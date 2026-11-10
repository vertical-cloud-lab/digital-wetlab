import sys, json, urllib.request, os
BASE="http://169.254.51.252:31950"
H={"Opentrons-Version":"3","Content-Type":"application/json"}
STATE=os.path.expanduser("~/ot2_ymin2/state.json")

def req(method, path, body=None):
    data=json.dumps(body).encode() if body is not None else None
    r=urllib.request.Request(BASE+path, data=data, headers=H, method=method)
    with urllib.request.urlopen(r, timeout=120) as resp:
        return json.loads(resp.read().decode())

def load_state():
    return json.load(open(STATE)) if os.path.exists(STATE) else {}
def save_state(s):
    json.dump(s, open(STATE,"w"))

def cmd(runid, body, wait=True):
    q="?waitUntilComplete=true" if wait else ""
    return req("POST", f"/maintenance_runs/{runid}/commands{q}", {"data":body})

def main():
    a=sys.argv[1]
    s=load_state()
    if a=="init":
        r=req("POST","/maintenance_runs",{"data":{}})
        runid=r["data"]["id"]
        s={"run":runid}
        # load pipette
        lp=cmd(runid, {"commandType":"loadPipette","params":{"pipetteName":"p300_single_gen2","mount":"left"}})
        s["pip"]=lp["data"]["result"]["pipetteId"]
        save_state(s)
        # home
        hm=cmd(runid, {"commandType":"home","params":{}})
        print("run",runid,"pip",s["pip"],"home",hm["data"]["status"])
    elif a=="move":
        x,y,z=float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])
        minz=float(sys.argv[5]) if (len(sys.argv)>5 and sys.argv[5] not in ("","-","none")) else None
        fd = (len(sys.argv)>6 and sys.argv[6]=="direct")
        params={"pipetteId":s["pip"],"coordinates":{"x":x,"y":y,"z":z},"forceDirect":fd}
        if minz is not None: params["minimumZHeight"]=minz
        c=cmd(s["run"], {"commandType":"moveToCoordinates","params":params})
        st=c["data"]["status"]
        print("move",x,y,z,"->",st)
        if st=="failed": print(json.dumps(c["data"].get("error",{}))[:400])
    elif a=="droptip":
        c=cmd(s["run"], {"commandType":"dropTipInPlace","params":{"pipetteId":s["pip"]}})
        print("droptip ->", c["data"]["status"])
        if c["data"]["status"]=="failed": print(json.dumps(c["data"].get("error",{}))[:400])
    elif a=="home":
        c=cmd(s["run"], {"commandType":"home","params":{}})
        print("home ->", c["data"]["status"])
    elif a=="savepos":
        c=cmd(s["run"], {"commandType":"savePosition","params":{"pipetteId":s["pip"]}})
        print(json.dumps(c["data"].get("result",{})))
    elif a=="delete":
        rid=s["run"]; req("DELETE", "/maintenance_runs/"+rid)
        print("deleted", s["run"])
    else:
        print("unknown", a)

main()
