# PI HANDOFF CHECKLIST
## ACS-PRF Proposal Final Submission Preparation

This checklist guides you through the final steps to complete your ACS-PRF proposal by adding the required experimental preliminary results.

---

## CURRENT STATUS

**Document:** `drafts/draft.tex`  
**Word Count:** 4,843 words (⚠️ EXCEEDS 3,900-word limit)  
**Compliance Status:** ❌ NON-COMPLIANT

**Action Required:** The proposal must be edited to ~3,883 words and saved as `draft_edited.tex` before figure insertion.

---

## FIGURES TO ADD

### 1. BaSO₄ Experimental Results
**Purpose:** Demonstrate the OT-2 robotic workflow with a proof-of-concept precipitation experiment

**File to Create:**  
`preliminary_results/baso4_results.png`

**Requirements:**
- Photograph or composite image showing a 96-well plate with BaSO₄ precipitation
- Should clearly show precipitation gradient or pattern across wells
- Recommended resolution: ≥300 DPI for publication quality
- File format: PNG (preferred) or PDF

**LaTeX Code to Add:**
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{../preliminary_results/baso4_results.png}
\caption{Preliminary BaSO\textsubscript{4} precipitation experiment demonstrating the high-throughput OT-2 workflow. A 96-well microplate was prepared with varying concentrations of Ba\textsuperscript{2+} and SO\textsubscript{4}\textsuperscript{2-} in NaCl brines (0.5--5~molal) at 25~$^\circ$C. Visible turbidity indicates precipitation.}
\label{fig:baso4_results}
\end{figure}
```

**Suggested Insertion Point:** After the TODO comment on line 59, or in a new "Preliminary Results" subsection

---

### 2. PbS or FeS Precipitate Photograph
**Purpose:** Show visible precipitate formation of the target sulfide mineral

**File to Create:**  
`preliminary_results/pbs_photo.png`

(or `fes_photo.png` if FeS is used instead)

**Requirements:**
- Clear photograph showing dark precipitate formation in solution or well
- Label should indicate the mineral (PbS or FeS)
- Recommended resolution: ≥300 DPI
- File format: PNG (preferred) or PDF

**LaTeX Code to Add:**
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.5\textwidth]{../preliminary_results/pbs_photo.png}
\caption{Lead sulfide (PbS, galena) precipitation from reaction of Pb\textsuperscript{2+} and HS\textsuperscript{-} in a NaCl brine. The characteristic black precipitate forms rapidly upon mixing.}
\label{fig:pbs_photo}
\end{figure}
```

**Suggested Insertion Point:** In the same area as the BaSO₄ figure, or in the introduction when first mentioning PbS

---

### 3. Fig:aim2 Placeholder Replacement
**Status:** Currently has a placeholder box  
**File to Create:**  
`../grants/acs-prf/figures/workflow-diagrams/aim2_analysis_pipeline.png`

(or use one of the existing figures like `precipitation_boundary_map.png`)

**Current LaTeX Code (line ~134):**
```latex
\begin{wrapfigure}{r}{0.4\textwidth}
\centering
\vspace{-1.5em}
\fbox{\rule{0pt}{1.5in}\rule{0.35\textwidth}{0pt}}
\caption{Aim~2 analysis pipeline...}
\label{fig:aim2}
\vspace{-1em}
\end{wrapfigure}
```

**Action Required:**
Replace the `\fbox{\rule{0pt}{1.5in}\rule{0.35\textwidth}{0pt}}` line with:
```latex
\includegraphics[width=0.35\textwidth]{../grants/acs-prf/figures/workflow-diagrams/aim2_analysis_pipeline.png}
```

---

## STEP-BY-STEP INSTRUCTIONS

### Step 1: Prepare Your Images
1. Take/create the BaSO₄ experimental photograph → save as `preliminary_results/baso4_results.png`
2. Take/create the PbS (or FeS) precipitate photograph → save as `preliminary_results/pbs_photo.png`
3. Create or select the Aim 2 analysis pipeline figure → save as indicated above

### Step 2: Verify File Paths
Ensure these files exist with EXACT filenames:
- [ ] `digital-wetlab-private - Copy/preliminary_results/baso4_results.png`
- [ ] `digital-wetlab-private - Copy/preliminary_results/pbs_photo.png`

From the `drafts/` directory, these paths will be referenced as:
- `../preliminary_results/baso4_results.png`
- `../preliminary_results/pbs_photo.png`

### Step 3: Edit draft_edited.tex
**CRITICAL:** Work on `draft_edited.tex` (the compliant ~3,883-word version), NOT `draft.tex`

1. Remove or comment out the TODO on line 59
2. Insert the BaSO₄ figure LaTeX code (see above)
3. Insert the PbS photo LaTeX code (see above)
4. Replace the placeholder box in fig:aim2 with actual `\includegraphics` command
5. Save the file

### Step 4: Compile and Verify
1. Compile the LaTeX document:
   ```bash
   cd drafts/
   pdflatex draft_edited.tex
   bibtex draft_edited
   pdflatex draft_edited.tex
   pdflatex draft_edited.tex
   ```

2. Open `draft_edited.pdf` and visually confirm:
   - [ ] BaSO₄ figure appears correctly
   - [ ] PbS (or FeS) photo appears correctly
   - [ ] Fig:aim2 shows actual figure (not placeholder box)
   - [ ] All figure captions are readable
   - [ ] Figures are high quality (not pixelated)
   - [ ] Figure references in text match the figure labels

3. Check word count:
   ```bash
   cat draft_edited.wordcount
   ```
   Should be ≤3,900 words

### Step 5: Final Pre-Submission Checks
- [ ] All TODO comments removed
- [ ] All placeholder boxes replaced with real figures
- [ ] Word count compliant (≤3,900 words)
- [ ] All figures appear in the PDF
- [ ] Bibliography compiles without errors
- [ ] No LaTeX compilation errors or warnings about missing references

---

## IMPORTANT NOTES

⚠️ **Filename Matching:** The filenames in your LaTeX `\includegraphics` commands must match the actual image files EXACTLY (including capitalization).

⚠️ **Path Relativity:** All paths are relative to the `drafts/` directory. The `../preliminary_results/` prefix navigates up one directory level then into the preliminary_results folder.

⚠️ **No Code Changes:** Once the image files are in place with the correct names, no further LaTeX source code changes are required.

⚠️ **Use draft_edited.tex:** The compliant version is `draft_edited.tex`, not `draft.tex`.

---

## TROUBLESHOOTING

**Problem:** Figure doesn't appear in PDF  
**Solution:** 
- Check file path is correct relative to drafts/ directory
- Verify filename matches exactly (case-sensitive)
- Ensure image file format is supported (.png, .pdf, .jpg)
- Check LaTeX log for error messages

**Problem:** Figure is low quality/pixelated  
**Solution:**
- Replace with higher resolution image (≥300 DPI)
- Use vector format (.pdf) if possible
- Ensure source image is high quality

**Problem:** LaTeX won't compile  
**Solution:**
- Check for unclosed braces {} in caption or label
- Verify all required packages are loaded (graphicx, etc.)
- Check LaTeX log file for specific error line

---

## QUESTIONS?

If you encounter issues, check:
1. LaTeX log file (`draft_edited.log`) for specific errors
2. That all image files exist in the correct locations
3. That you're compiling the correct file (draft_edited.tex)

---

**Last Updated:** Generated from automated LaTeX source analysis
**Document Version:** draft.tex (4,843 words, non-compliant baseline)
**Target Version:** draft_edited.tex (≤3,900 words, compliant)
