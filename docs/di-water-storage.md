# How long deionized water keeps, and whether it can sit in an open container

Asked by Timothy Commins on [issue 80](https://github.com/vertical-cloud-lab/digital-wetlab/issues/80)
on 2026-10-27, for the lead (PbS) experiments. The lab's DI water comes free from the Chem Stores
breakroom and is kept in an HDPE gallon jug filled in March
([byu-vcl 15](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3993875085)).

## Short answer

- **DI water has no expiry date, but it starts losing purity as soon as it leaves the purifier.**
  ISO 3696, the international standard for lab water, gives no shelf life. It recommends not
  storing the two purest grades at all, but making them as needed. Water that is stored goes in
  "suitable, inert, clean, airtight, full containers", each kept for one grade of water only
  ([ISO 3696](#sources), clause 6).
- **Keeping it in an open container for days or weeks isn't practical.** Four things happen:
  1. **CO₂ from the air dissolves in it** within seconds to hours. That brings it to pH 5.6 and
     about 1 µS/cm, and it stays there. This doesn't get worse with time.
  2. **Fumes dissolve in it.** In the hood, that means ammonia and H₂S from the ammonium sulfide.
  3. **Dust and bacteria get in, and the bacteria grow.** This is the part that gets worse with
     time: in the papers below, counts climb to 10⁵–10⁷ per mL within days to weeks and then
     stay there for months.
  4. **It evaporates, and it slowly leaches the container.** Neither matters much for the water
     itself.
- **For the lead experiments, the CO₂ doesn't matter, but the bacteria, dust and fumes are
  variables nobody controls.** The jug from March is seven months old. Pour it out, rinse the
  jug, and fetch fresh water shortly before making stocks. Keep it capped and use it within about a
  week ([what to do](#what-to-do)).

## What happens to DI water left open

### 1. It takes up CO₂ (seconds to hours, then steady)

Pure water conducts 0.055 µS/cm (18.2 MΩ·cm). CO₂ from the air dissolves as carbonic acid, and
the water ends up at these values. They're PHREEQC equilibrium values for 25 °C at BYU's altitude
(about 1,400 m, 0.85 atm); the script and the full table, including 20 °C and sea level, are in
[`di-water-checks/`](di-water-checks/results.txt).

| air | pH | conductivity (µS/cm) | resistivity (MΩ·cm) | dissolved CO₂ + carbonate (µM) |
| --- | --- | --- | --- | --- |
| outdoor CO₂, 425 ppm | 5.64 | 0.90 | 1.1 | 14 |
| occupied room, 1,000 ppm | 5.45 | 1.38 | 0.72 | 31 |
| crowded room, 2,000 ppm | 5.30 | 1.96 | 0.51 | 60 |

- **Speed.** Water dispensed into air reaches 1–2 µS/cm "within seconds of collection"
  ([Gleichauf & Knepper 2016](#sources), a trade-journal note). A jug that sits still takes longer,
  but every pour and slosh mixes air in.
- **The standards build this in.**
  - ISO 3696 says its conductivity limits for grades 1 and 2 "apply to freshly prepared water",
    because CO₂, and alkalis from glass, dissolve during storage. Its test for grade 3 water keeps
    CO₂ out with a soda-lime guard tube on the flask.
  - The pharmacopeia test (USP <645>) stirs water in air until CO₂ uptake levels off, then
    allows up to 2.1 µS/cm.
- **This sets a floor, not a countdown.** Water that has touched air sits at about 1 µS/cm and
  stays there. That is about ISO's grade 2 limit (1 µS/cm) and well inside grade 3 (5 µS/cm).
  Once it's in a jug, the lab's water is grade 2–3 water, whatever the breakroom unit produces.
  That is fine for 10 mM stocks ([below](#what-it-means-for-the-lead-experiments)).

### 2. It takes up fumes

ISO 3696 names "absorption of atmospheric carbon dioxide and of any other impurities present in
the laboratory atmosphere" as one of the two main ways stored water gets contaminated. In the hood
with the ammonium sulfide open, that means ammonia and H₂S, both of which dissolve in water. Keep
the water capped, and outside the hood except while pouring.

### 3. Dust and bacteria get in, and bacteria grow

Bacteria grow in distilled and deionized water on the traces of organic matter it still holds.
Water straight from a purifier isn't necessarily sterile either. Bacteria live inside working lab
and industrial ultrapure-water systems, including the final polishing loop
([McFeters et al. 1993; Kulakov et al. 2002](#sources)).

| study | water | what grew |
| --- | --- | --- |
| [Favero et al. 1971](#sources), *Science* | hospital distilled water | *Pseudomonas aeruginosa* grew "relatively fast" to high counts that "remain stable for long periods of time" |
| [Carson et al. 1973](#sources) | distilled water | *P. cepacia* (now *Burkholderia cepacia*) reached and held 10⁶–10⁷ per mL, anywhere from 18 to 42 °C |
| [Kayser et al. 1975](#sources) | a storage reservoir of ultrapure distilled water, and commercial distilled water | *P. aeruginosa* and *P. cepacia* grew rapidly to about 10⁵ per mL. Once the reservoir was contaminated, it stayed contaminated. |
| [Carson et al. 1978](#sources) | commercial distilled water | mycobacteria doubled every 8–15 h at 25 °C, reached 10⁵–10⁶ per mL, and declined only slightly over a year |
| [McAlister et al. 2002](#sources) | ultrapure water | bacteria from industrial ultrapure-water systems grew rapidly to about 10⁶ per mL, then held there for 6 months or more |

At 8–15 hours per doubling, going from 1 cell per mL to 10⁵ per mL takes about 17 doublings,
which is 6–10 days. That is my estimate from these papers, not a measurement of the lab's water.
So a few days is roughly how long contaminated water takes to reach high counts, and after a few
weeks it has reached its plateau. **A cap doesn't stop this.** Bacteria already in the water
keep growing, and a storage reservoir that was once contaminated stayed contaminated
([Kayser et al. 1975](#sources)). What a cap does is keep more bacteria, dust and fumes from
getting in.

**Why it matters for precipitation experiments.** At these counts, neither the bacteria nor the
dust would likely show up by eye or in a 600 nm reading. But every cell or grain is a surface that a
precipitate can form on (heterogeneous nucleation; [Kashchiev & van Rosmalen 2003](#sources)).
In an experiment that measures when and where precipitate first appears, that's an uncontrolled
variable.

**Refilled squeeze bottles are a known source of contamination.** Washington State's health
department and the CDC traced 22 false fungal "infections" at a clinic in 2024 to saline squeeze
bottles that had been refilled and reused
([Yomogida et al. 2026](#sources)). That was saline in a clinic, not DI water in a lab, but
topping up a bottle works the same way in both.

### 4. It evaporates, and slowly leaches the container

ISO 3696 names "dissolution of soluble constituents from glass or plastics containers" as the
other main way stored water gets contaminated. Its sampling clause names polyethylene and
polypropylene as suitable inert plastics (clause 5), so the lab's HDPE jug is a reasonable
choice, as
[noted in March](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3993989121).
Leaching matters for trace analysis at µg/L, not for 10 mM stocks. Evaporation from an open
container does little harm to the water itself, but it concentrates stock solutions, so keep
those capped too.

### What a cap doesn't do

A cap doesn't remove dissolved O₂. Any water that has touched air holds about 7 mg/L of O₂ at
BYU (6.99 mg/L at 25 °C, 7.70 at 20 °C; [results](di-water-checks/results.txt)), sealed or not.
Only sparging with N₂ (or boiling and cooling under N₂) removes it.

## What it means for the lead experiments

- **The CO₂ doesn't matter here.** Air adds about 14 µM of dissolved carbonate, or 31–60 µM
  indoors at 1,000–2,000 ppm CO₂. That's 0.1–0.6% of a 10 mM stock. A 10 mM lead(II) nitrate
  stock made in this water stays undersaturated with lead carbonate (saturation index −1.0, or
  −0.56 at 2,000 ppm CO₂) and with lead hydroxide (−0.7 to −0.9)
  ([PHREEQC, wateq4f.dat](di-water-checks/results.txt)).
- **The bacteria, dust and fumes matter a little, and nobody knows what is in the March jug.**
  Seven months is long enough for any bacteria in it to have reached their plateau. Fresh water
  costs nothing, so there's no reason to use the old water.
- **O₂ matters for the sulfide, not the lead.** Dissolved O₂ slowly oxidizes sulfide
  ([Chen & Morris 1972](#sources)). That's one reason the
  [materials list](https://github.com/vertical-cloud-lab/digital-wetlab/blob/9605f21/docs/lead-pbs-materials-and-steps.md)
  says to make the sulfide stock fresh each day, in a nearly full, capped tube. The iron (FeS) work later needs water that has
  been sparged with N₂, whatever container it's kept in.

## What to do

1. **Pour out the March water.** Don't top it up.
2. **Rinse the jug** two or three times with fresh DI water, or replace it with a new HDPE or
   polypropylene bottle. Use it only for DI water (ISO 3696, clause 6).
3. **Fetch water shortly before making stocks.** Fill the bottle nearly full and cap it. Keep it
   out of the hood except while pouring.
4. **Use it within about a week.** That's my suggestion from the growth rates above, not a limit
   from a standard. Throw it out sooner if it looks cloudy, has floaters or slime on the walls,
   or smells.
5. **Pour, don't dip.** Pour what you need into a clean tube or beaker. Never pipette straight
   from the jug, and never pour water back in.
6. **Wash bottle:** empty it and refill it with fresh water each day you use it, rather than
   topping it up.
7. **Optional: a conductivity meter that reads down to 1 µS/cm.** Nothing on record says what
   the breakroom unit produces, so it's worth checking each batch. Fresh water that has touched
   air reads about 1–2 µS/cm, and ISO grade 3 allows up to 5 µS/cm.
8. **Optional, for quantitative plates later:** filter stocks through a 0.2 µm syringe filter
   to remove dust and bacteria.

## Sources

Peer-reviewed:

- Favero MS, Carson LA, Bond WW, Petersen NJ (1971). *Pseudomonas aeruginosa*: growth in
  distilled water from hospitals. *Science* 173:836–838.
  [doi:10.1126/science.173.3999.836](https://doi.org/10.1126/science.173.3999.836)
- Carson LA, Favero MS, Bond WW, Petersen NJ (1973). Morphological, biochemical, and growth
  characteristics of *Pseudomonas cepacia* from distilled water. *Appl. Microbiol.* 25:476–483.
  [doi:10.1128/am.25.3.476-483.1973](https://doi.org/10.1128/am.25.3.476-483.1973)
  (free: [PMC380831](https://pmc.ncbi.nlm.nih.gov/articles/PMC380831/))
- Kayser WV, Hickman KC, Bond WW, Favero MS, Carson LA (1975). Bacteriological evaluation of an
  ultra-pure water-distilling system. *Appl. Microbiol.* 30:704–706.
  [doi:10.1128/am.30.4.704-706.1975](https://doi.org/10.1128/am.30.4.704-706.1975)
  (free: [PMC187253](https://pmc.ncbi.nlm.nih.gov/articles/PMC187253/))
- Carson LA, Petersen NJ, Favero MS, Aguero SM (1978). Growth characteristics of atypical
  mycobacteria in water and their comparative resistance to disinfectants. *Appl. Environ.
  Microbiol.* 36:839–846.
  [doi:10.1128/aem.36.6.839-846.1978](https://doi.org/10.1128/aem.36.6.839-846.1978)
  (free: [PMC243155](https://pmc.ncbi.nlm.nih.gov/articles/PMC243155/))
- McFeters GA, Broadaway SC, Pyle BH, Egozy Y (1993). Distribution of bacteria within operating
  laboratory water purification systems. *Appl. Environ. Microbiol.* 59:1410–1415.
  [doi:10.1128/aem.59.5.1410-1415.1993](https://doi.org/10.1128/aem.59.5.1410-1415.1993)
  (free: [PMC182097](https://pmc.ncbi.nlm.nih.gov/articles/PMC182097/))
- Kulakov LA, McAlister MB, Ogden KL, Larkin MJ, O'Hanlon JF (2002). Analysis of bacteria
  contaminating ultrapure water in industrial systems. *Appl. Environ. Microbiol.* 68:1548–1555.
  [doi:10.1128/AEM.68.4.1548-1555.2002](https://doi.org/10.1128/AEM.68.4.1548-1555.2002)
  (free: [PMC123900](https://pmc.ncbi.nlm.nih.gov/articles/PMC123900/))
- McAlister MB, Kulakov LA, O'Hanlon JF, Larkin MJ, Ogden KL (2002). Survival and nutritional
  requirements of three bacteria isolated from ultrapure water. *J. Ind. Microbiol. Biotechnol.*
  29:75–82. [doi:10.1038/sj.jim.7000273](https://doi.org/10.1038/sj.jim.7000273)
- Kashchiev D, van Rosmalen GM (2003). Review: Nucleation in solutions revisited. *Cryst. Res.
  Technol.* 38:555–574. [doi:10.1002/crat.200310070](https://doi.org/10.1002/crat.200310070)
- Chen KY, Morris JC (1972). Kinetics of oxidation of aqueous sulfide by oxygen. *Environ. Sci.
  Technol.* 6:529–537. [doi:10.1021/es60065a008](https://doi.org/10.1021/es60065a008)
- Yomogida KS et al. (2026). Pseudo-outbreak of *Purpureocillium lilacinum* skin infections at a
  dermatology clinic, Washington, 2024. *MMWR* 75:64–67.
  [doi:10.15585/mmwr.mm7505a2](https://doi.org/10.15585/mmwr.mm7505a2)

Standards and other:

- ISO 3696:1987, *Water for analytical laboratory use: specification and test methods*
  ([ISO page](https://www.iso.org/standard/9169.html)). Clause 6 (storage), the requirements
  table and its notes, and clause 5 (containers) were read from the
  [publisher's preview pages](https://cdn.standards.iteh.ai/samples/9169/c86dc332be2847eebd009b52ef8b00a5/ISO-3696-1987.pdf).
- USP <645>, *Water Conductivity*, stage 2. Read through secondary summaries (Mettler-Toledo,
  SUEZ, Metrohm), not the chapter itself.
- Gleichauf G, Knepper K (2016). The myths and truths of measuring pure water. *American
  Laboratory*, 7 November 2016
  ([link](https://americanlaboratory.com/914-Application-Notes/240483-The-Myths-and-Truths-of-Measuring-Pure-Water/)).
  A trade-journal note by Thermo Fisher staff, not peer-reviewed.
- Parkhurst DL, Appelo CAJ (2013). Description of input and examples for PHREEQC version 3.
  USGS Techniques and Methods 6-A43. [doi:10.3133/tm6A43](https://doi.org/10.3133/tm6A43).
  Run through [phreeqpython](https://github.com/Vitens/phreeqpython), with the bundled
  `phreeqc.dat` and the USGS `wateq4f.dat`.
