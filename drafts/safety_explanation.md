# Safety and Health Explanation

> **Project:** Pitzer Ion-Interaction Framework for Predicting Sulfide-Mineral Precipitation from Petroleum-Derived H₂S and Organic Acids in Produced-Water Brines

---

## Version A: Concise Form Entry (~450 words)

> *Copy-paste the text below into the ACS PRF application field: "PIs must describe any significant risks or hazards that may be encountered in the proposed work, and how these risks or hazards would be mitigated."*

The primary hazards in this project are (1) hydrogen sulfide (H₂S) released from NaHS solutions and (2) lead toxicity from PbCl₂ and Pb(NO₃)₂. Secondary hazards include corrosive acids and bases (HCl, NaOH, HNO₃), elevated temperatures (60–90 °C), and nitrogen asphyxiation risk from the glovebox atmosphere. Our mitigation strategy follows the ACS RAMP framework and the NIOSH hierarchy of controls.

**Engineering controls.** All sulfide and lead experiments are conducted with the Opentrons OT-2 liquid handler housed inside a chemical fume hood, providing continuous ventilation and H₂S containment. For Fe²⁺ campaigns requiring anoxic conditions, the OT-2 is placed inside an N₂ glovebox (O₂ < 5 ppm, continuously monitored), which also contains any H₂S generated. Adhesive plate seals are applied immediately after dispensing to minimize off-gassing. Elevated-temperature experiments use sealed borosilicate vials with PTFE-lined caps to contain H₂S at higher vapor pressures.

**Experimental design controls.** All experiments are conducted at pH ≥ 8, where HS⁻ dominates over H₂S(aq), maintaining negligible H₂S partial pressure. Organic acids are used as sodium salts (sodium acetate, sodium propionate) to reduce corrosivity. All reactions are performed at microplate scale (≤300 µL per well), minimizing chemical inventory at any given time.

**Administrative controls.** All work operates under BYU's Chemical Hygiene Plan (29 CFR 1910.1450). Written SOPs will be developed before experiments begin for NaHS preparation, Pb²⁺ handling and waste, Fe²⁺ glovebox protocols, and high-temperature operations. All personnel (1 M.S. student, 2 undergraduates) will complete BYU EH&S laboratory safety training and project-specific training on H₂S, lead, glovebox, and OT-2 hazards before beginning work. A buddy system ensures no lone work with sulfide or lead solutions. Pre-experiment safety briefings (job safety analyses) will be conducted before each new campaign. Near-misses are reported and reviewed at weekly lab meetings.

**PPE.** Safety glasses or splash goggles, nitrile gloves (double-gloving for Pb²⁺), lab coat, and closed-toe shoes are required. An H₂S personal gas detector (alarm at 5 ppm STEL) is worn during all sulfide experiments.

**Waste disposal.** Lead-containing solutions and contaminated consumables are collected as hazardous waste through BYU EH&S — never discharged to drain. Sulfide waste is oxidized with dilute H₂O₂ or bleach in the fume hood before disposal, or collected directly as hazardous waste.

**Emergency preparedness.** Eyewash, safety shower, spill kits, and fire extinguisher are maintained and verified before each campaign. For H₂S detector alarm (≥5 ppm), all operations cease, the area is evacuated, and BYU emergency services are contacted. Emergency contacts include BYU EH&S and Poison Control.

---

## Version B: Full Safety Document (Detailed Backup)

This safety plan follows the ACS RAMP framework (Recognize hazards, Assess risks, Minimize risks, Prepare for emergencies) as recommended by the ACS Center for Lab Safety, and incorporates principles from the ACS *Guidelines for Chemical Laboratory Safety in Academic Institutions* (2016), the APLU *Guide to Implementing a Safety Culture in Our Universities* (2016), and the CCPS/AIChE *Guidelines for Risk-Based Process Safety* (2007).

---

## Safety Culture and PI Commitment

The PI is committed to fostering a proactive safety culture in which safety is a core value, not merely a compliance obligation (APLU 2016; CCPS Pillar 1: Commit to Process Safety). All laboratory personnel will be expected to raise safety concerns without hesitation, report near-misses, and treat every incident or deviation as a learning opportunity (CCPS Pillar 4: Learn from Experience). The PI will lead by example by conducting pre-experiment safety briefings before each new experimental campaign, maintaining accessible Safety Data Sheets (SDSs) for all reagents (per GHS/OSHA Hazard Communication Standard), and ensuring that all work operates under BYU's institutional Chemical Hygiene Plan (CHP) as required by the OSHA Laboratory Standard (29 CFR 1910.1450).

---

## 1. Recognize Hazards

This project involves the following chemical, physical, and environmental hazards, identified through review of SDSs, GHS classifications, and prior literature:

**Chemical hazards:**

- **Hydrogen sulfide (H₂S).** NaHS solutions release H₂S gas upon acidification. H₂S is acutely toxic (OSHA TWA: 1 ppm; STEL: 5 ppm) and flammable. GHS: H220, H330, H400.
- **Lead compounds.** PbCl₂ and Pb(NO₃)₂ are toxic by ingestion, inhalation, and skin absorption. Lead is a cumulative toxin with reproductive and neurological effects. GHS: H302, H332, H360, H373.
- **Iron(II) salts.** FeSO₄·7H₂O and FeCl₂·4H₂O are irritants. GHS: H302, H315, H319.
- **Concentrated acids and bases.** HCl (~12 M) and NaOH pellets are corrosive (GHS: H314). Trace-metal-grade HNO₃ (~70%) is a strong oxidizer and corrosive.
- **Organic acids.** Glacial acetic acid is flammable and corrosive (GHS: H226, H314). Sodium acetate, sodium propionate, and cyclohexane carboxylic acid are low-hazard irritants requiring standard PPE.
- **Hydroxylamine hydrochloride.** Harmful if swallowed (H302), irritant (H315, H319).

**Chemical incompatibilities (per ACS Academic Safety Guidelines):**

- Oxidizers (HNO₃) stored separately from reducing agents (hydroxylamine, NaHS).
- Acids (HCl, acetic acid) stored separately from bases (NaOH, Na₂CO₃).
- Lead salts stored in secondary containment with clear labeling.

**Physical hazards:**

- **Elevated temperatures.** Heater-shaker module and sealed glass vials at 60–90 °C — burn risk and increased H₂S vapor pressure.
- **Automated robotic equipment.** Opentrons OT-2 moving pipette heads and heater-shaker with mechanical pinch hazards.
- **Pressurized gas.** High-purity N₂ cylinder for water deoxygenation and glovebox atmosphere.

---

## 2. Assess Risks

Risk assessment follows the severity × likelihood matrix approach recommended by the ACS Center for Lab Safety and CCPS Pillar 2 (Understand Hazard & Risk):

| Hazard                                | Severity                         | Likelihood (with controls)                                      | Overall Risk                |
| ------------------------------------- | -------------------------------- | --------------------------------------------------------------- | --------------------------- |
| H₂S inhalation from NaHS solutions    | High (acute toxicity at low ppm) | Low (fume hood + pH ≥ 8 + plate seals)                          | **Medium — primary hazard** |
| Lead exposure (dermal/ingestion)      | High (cumulative toxin)          | Low (PPE + small microplate volumes)                            | **Medium**                  |
| Acid/base burns (HCl, NaOH, HNO₃)     | Moderate (corrosive)             | Low (standard lab handling, PPE)                                | Low                         |
| Burns from heated vials (60–90 °C)    | Moderate                         | Low (heater-shaker module, tongs)                               | Low                         |
| N₂ asphyxiation (glovebox atmosphere) | High (in enclosed spaces)        | Very low (standard glovebox in ventilated room with O₂ monitor) | Low                         |
| Chemical incompatibility reaction     | Moderate                         | Very low (segregated storage, SOPs)                             | Low                         |

The highest-risk operations are (1) preparation and handling of NaHS stock solutions and (2) handling of lead-containing solutions. Both are mitigated by layered controls below.

---

## 3. Minimize Risks

The mitigation strategy follows the hierarchy of controls (elimination → substitution → engineering → administrative → PPE), consistent with NIOSH recommendations and the ACS Academic Safety Guidelines. Layered controls are applied to the two primary hazards (CCPS Pillar 3: Manage Risks).

### Engineering Controls

- **Chemical fume hood.** All sulfide and lead experiments are conducted with the OT-2 housed inside a chemical fume hood, providing continuous ventilation and containment of H₂S vapors.
- **N₂ inert-atmosphere glovebox.** For Fe²⁺ campaigns, the OT-2 is placed inside a general-purpose N₂ glovebox (O₂ < 5 ppm, continuously monitored) to prevent iron oxidation. The enclosed atmosphere also contains any H₂S generated.
- **Adhesive plate seals.** Applied immediately after dispensing to minimize H₂S off-gassing and evaporation from 96-well plates.
- **Sealed glass vials.** Elevated-temperature experiments (60–90 °C) use borosilicate vials with PTFE-lined screw caps to contain H₂S at elevated vapor pressures.
- **Filter pipette tips.** Used for sulfide and metal stock dispensing to prevent cross-contamination and protect the pipette from corrosive solutions.
- **Chemically resistant well plates.** Polypropylene 96-well plates selected for compatibility with HS⁻/H₂S solutions.

### Experimental Design Controls (Substitution/Elimination)

- **Working at pH ≥ 8.** Ensures HS⁻ dominance over H₂S(aq), maintaining negligible H₂S partial pressure during experiments.
- **Organic acids as sodium salts.** Sodium acetate and sodium propionate are used instead of free acid forms, reducing corrosivity and avoiding unnecessary pH adjustment.
- **Small volumes.** All experiments use microplate-scale volumes (≤300 µL per well), minimizing chemical inventory at any given time.
- **Fresh Fe²⁺ preparation.** Solutions prepared daily from solid salts in deoxygenated water, with 10% verified by 1,10-phenanthroline assay (510 nm); batches with >2% Fe³⁺ are discarded.

### Administrative Controls

- **Chemical Hygiene Plan (CHP).** All work operates under BYU's institutional CHP as required by the OSHA Laboratory Standard (29 CFR 1910.1450). The departmental Chemical Hygiene Officer will be consulted during setup.
- **Standard operating procedures (SOPs).** Written SOPs will be developed and approved *before* any experimental work begins for: NaHS stock preparation, Pb²⁺ handling and waste collection, Fe²⁺ glovebox protocols, OT-2 operation, and high-temperature vial handling. SOPs will be reviewed whenever procedures change (management of change, per CCPS).
- **Pre-experiment safety briefings.** Before each new experimental campaign (e.g., first FeS plate, first Pb²⁺ plate, first high-temperature run), the PI will conduct a job safety analysis (JSA) with all involved personnel to review hazards, controls, and emergency procedures specific to that campaign.
- **Training.** All personnel (1 M.S. student, 2 undergraduate researchers) will complete:
  - BYU Environmental Health & Safety (EH&S) laboratory safety training (chemical hygiene, hazardous waste, compressed gas) before beginning laboratory work.
  - Project-specific training on H₂S hazards, lead handling, glovebox operation, and OT-2 safety, provided by the PI.
  - Periodic refresher training at 6-month intervals and whenever procedures change (per APLU 2016 recommendation for ongoing training).
- **Safety Data Sheets.** SDSs for all reagents will be maintained in a clearly labeled binder at the lab entrance and electronically, reviewed with personnel before first use of each chemical (per GHS/OSHA Hazard Communication Standard).
- **Buddy system.** No lone work with H₂S-generating or lead-containing solutions. At least two trained personnel will be present during sulfide dispensing operations.
- **Near-miss reporting.** All near-misses, unexpected observations (e.g., unusual odors, unexpected color changes), and equipment malfunctions will be documented and reviewed at weekly lab meetings, consistent with APLU and CCPS Pillar 4 (Learn from Experience) recommendations.
- **Chemical storage.** Chemicals are stored according to compatibility (oxidizers separated from reducing agents, acids separated from bases, lead salts in labeled secondary containment), consistent with the ACS Academic Safety Guidelines.
- **PI experience.** The PI has prior experience handling battery electrolytes, concentrated nitric acid, saturated KOH, and reactive nanomaterials.

### Personal Protective Equipment (PPE)

- Safety glasses or chemical splash goggles (required at all times in the lab).
- Nitrile gloves (required for all operations; double-gloving for Pb²⁺ handling).
- Lab coat (required at all times in the lab).
- Closed-toe shoes (required).

### Environmental Monitoring

- **H₂S personal gas detector** (e.g., Honeywell BW Solo or BW Clip): continuous single-gas monitor worn during all sulfide experiments, with audible/visual alarm at 5 ppm (STEL).
- **Glovebox O₂ sensor**: continuous electrochemical monitoring to maintain O₂ < 5 ppm.
- **Temperature/humidity data logger**: continuous monitoring inside fume hood and glovebox workspace.

---

## 4. Prepare for Emergencies

### Emergency Equipment (verified before each experimental campaign)

- **Eyewash station and safety shower** in the laboratory (inspected per ANSI Z358.1).
- **Fire extinguisher** (ABC type) accessible within 50 feet.
- **Chemical spill kits** containing absorbent materials, neutralizing agents, and disposal bags for acid/base and heavy-metal spills.
- **First aid kit** stocked and accessible.

### Emergency Response Procedures

- **H₂S exposure:** Immediately evacuate to fresh air. If H₂S detector alarms (≥5 ppm), cease all operations, evacuate the area, and contact BYU emergency services (911) and EH&S. Administer supplemental oxygen if trained and available. Seek medical attention for any symptomatic exposure.
- **Lead exposure/spill:** Remove contaminated clothing, wash affected skin thoroughly with soap and water. For spills, contain with absorbent from spill kit, collect in labeled hazardous waste container. Do not dry-sweep lead-containing residues.
- **Acid/base splash or burn:** Flush affected area with water for at least 15 minutes using eyewash or safety shower. Remove contaminated clothing. Seek medical attention.
- **Thermal burn (60–90 °C vials):** Cool the affected area with running water. Seek medical attention for burns larger than a quarter or on sensitive areas.
- **N₂-related O₂ depletion:** If area O₂ monitor alarms or symptoms of lightheadedness occur, evacuate immediately and ventilate the area.

### Waste Disposal

- **Lead-containing waste:** All Pb²⁺-containing solutions, well plates, and contaminated consumables are collected as hazardous waste and disposed through BYU EH&S hazardous waste program. Lead waste is never discharged to the drain.
- **Sulfide-containing waste:** NaHS solutions are neutralized (oxidized with dilute H₂O₂ or bleach to convert HS⁻ to sulfate) in the fume hood before disposal, or collected directly as hazardous waste.
- **Acid/base waste:** Collected in labeled waste containers and disposed through BYU EH&S.
- **Sharps and broken glass:** Disposed in designated sharps containers.
- **General consumables:** Non-contaminated plasticware disposed as solid waste.

### Incident Investigation and Continuous Improvement

Any incident, near-miss, or safety concern will be investigated to identify root causes and corrective actions, documented, and reviewed at lab meetings. Lessons learned will be incorporated into updated SOPs and training materials (per CCPS Pillar 4: Learn from Experience; APLU 2016).

### Emergency Contact Information

- BYU Emergency Services: 911 (on campus) or (801) 422-2222
- BYU Environmental Health & Safety: (801) 422-3351
- PI cell phone: [to be provided]
- Poison Control: 1-800-222-1222

---

## References

- ACS, *Guidelines for Chemical Laboratory Safety in Academic Institutions* (2016)
- APLU Council Task Force on Laboratory Safety, *A Guide to Implementing a Safety Culture in Our Universities* (2016)
- AAPT, *Safety in Physics Education* (2001)
- South Dakota School of Mines and Technology, *Laboratory and Field Safety Guidelines* (2019–2020)
- CCPS/AIChE, *Guidelines for Risk-Based Process Safety* (2007) — Four pillars: Commit to Process Safety, Understand Hazard & Risk, Manage Risks, Learn from Experience
- ACS Center for Lab Safety, *Safety Basics & RAMP* (https://institute.acs.org/acs-center/lab-safety/safety-basics-and-ramp.html)
- Sigmann & McEwen, "Communicating Safety Information," in *ACS Guide to Scholarly Communication* (2020), DOI: 10.1021/acsguide.10301
- OSHA Laboratory Standard, 29 CFR 1910.1450
- OSHA Hydrogen Sulfide Standards, 29 CFR 1910.1000, Table Z-2
- OSHA Hazard Communication Standard (GHS), 29 CFR 1910.1200
- NIOSH Hierarchy of Controls (https://www.cdc.gov/niosh/topics/hierarchy/)
- ANSI/ISEA Z358.1 — Emergency Eyewash and Shower Equipment
