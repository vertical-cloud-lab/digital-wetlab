# Utah AI Convergence 2026 — Student Poster Competition Abstract

> **Event:** [Utah AI Convergence 2026](https://www.price.utah.edu/ai/convergence-2026), June 23–24, S.J. Quinney College of Law Building, University of Utah.
> **Track:** Student Poster Competition (research that uses or advances AI).
> **Limit:** 500 words for the main text (title, authors, and affiliations excluded).

## Title

A Self-Driving Wet Lab: Bayesian-Optimized Robotic Experiments for Predicting Mineral Scale Formation

## Authors

_To be completed by the submitting student(s) and advisor._

## Abstract

Sulfide-mineral scales such as FeS and PbS form when dissolved metal ions
react with HS⁻ in concentrated, multi-component brines, restricting flow and
fouling equipment during industrial water and energy operations. Quantitative
prediction of when and where these scales form depends on the Pitzer
ion-interaction model, yet roughly 48 binary and ternary interaction
parameters for the metal–sulfide and metal–organic-acid systems most relevant
to these brines have never been measured. Closing this gap requires
systematic precipitation measurements across about 30,000 conditions spanning
ionic strength (0.5–5 molal), pH (4–9), temperature (25–90 °C), and competing
ion concentrations—well beyond the throughput of conventional bottle tests.

We are building an automated wet-lab platform to make these measurements
tractable. An Opentrons OT-2 pipetting robot, controlled through its Python
API, dispenses stock solutions into microplates and logs every volume, well
position, and timestamp. Our first experiments use 96-well plates, and the
workflow is designed to scale to 384-well plates for higher throughput.
Precipitation is read out by three complementary methods used in our
proposals: visual binary scoring, low-cost camera imaging with automated
analysis, and microplate-reader absorbance/turbidity at 600 nm. We are also
integrating a wireless color sensor—replicating an open-source design from
the Acceleration Consortium—to give parallel, in-situ per-well color
readings without dedicated lab instruments.

As a tractable, low-hazard demonstration, we begin with barium sulfate
benchtesting. Combining BaCl₂ with Na₂SO₄ produces a white precipitate whose
onset is sharply sensitive to supersaturation and to background NaCl. Our
first automated run sweeps eight Ba²⁺ concentrations against a twelve-step
NaCl gradient at fixed sulfate, imaging each plate before and after sulfate
addition. These measured precipitation boundaries are overlaid on
saturation-index predictions from the PHREEQC Pitzer model, exercising the
full pipeline—liquid handling, sensing, and data capture—and exposing where
current parameters disagree with experiment.

AI then guides where to look next. Latin hypercube sampling fills the
high-dimensional composition space with broadly distributed initial
conditions, and Bayesian optimization with Gaussian-process surrogates
adaptively targets conditions near precipitation boundaries, where parameter
sensitivity is highest. Where measured boundaries deviate from PHREEQC
predictions by more than ±0.2 saturation-index units, new Pitzer parameters
are regressed by weighted nonlinear least-squares and assessed via 5-fold
cross-validation and held-out high-ionic-strength challenge splits.

The expected deliverable is a set of validated Pitzer parameters for
sulfide-scale prediction in industrially relevant brines, transferable to
standard thermodynamic databases. Because the OT-2 protocols, sensing, and
optimization loop are reagent-agnostic and software-defined, the same setup
provides a foundation for letting other researchers run their own automated
experiments through the cloud. We present the platform design, our first
barium sulfate results, and the Bayesian-optimization strategy that makes
this scale of parameter measurement tractable.
