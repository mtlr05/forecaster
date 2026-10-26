# MRI-compatible CED delivery: Brainlab, Renishaw and the Parkinson's trials
Checked October 25, 2026, against primary sources. Prompted by David's statement (Oct 25, 2026): "Brainlab and Renishaw do not have a cannula which can be used for CED which is MRI compatible."

## The 10-K sentence (exact context)
ClearPoint FY2025 10-K, Item 1, Competition, "Biologics and Drug Delivery" (https://www.sec.gov/Archives/edgar/data/1285550/000119312526111231/clpt-20251231.htm):
> "Drug delivery can be divided into two categories, those that use image-guidance and those that do not. Our main area of focus and expertise is on image-guided drug delivery, in particular as it relates to the use of MRI technology. Other companies, such as Brainlab and Renishaw plc, also offer systems such as navigational platforms and cannulas useful for drug delivery under MRI. These offerings are competitive with our products."
The sentence is generic: it names no product and doesn't say which company offers which item.

## Brainlab
- **iPlan Flow** (FDA 510(k) K053164, https://www.accessdata.fda.gov/cdrh_docs/pdf5/K053164.pdf) is planning software, "a dedicated tool for planning trajectories of intra-cranial catheters." It uses MR/DTI images to suggest likely volumes of fluid distribution. It is software, not a cannula.
- **Cranial Navigation and Elements** (K223288, K223552) are navigation and planning systems. Their indications include "intracranial catheter placement" and "catheter placement." They are navigation platforms, not cannulas.
- **Brainlab Flexible Catheter** (models 19770 and 19772; GUDID https://fda.report/GUDID/04056481006426):
  - Model 19772 is listed "In Commercial Distribution" and "MR Safe," with FDA product code HCA (ventricular catheter).
  - Its premarket submission is K123605, a 510(k) held by **MRI Interventions, Inc.** (ClearPoint's former name) for the "SmartFlow Flex Ventricular Catheter." That clearance covers cytarabine injection or CSF removal from the ventricles and is "not intended for implant" (https://www.accessdata.fda.gov/cdrh_docs/pdf12/K123605.pdf).
  - Inference, not confirmed by either company: this is a ClearPoint-designed (likely ClearPoint-made) catheter sold under the Brainlab name.
- **Brainlab catheter in published use.** Brainlab's catheter has been used for CED under MRI. In a DIPG study (J Neurosurg Pediatr 2021, https://thejns.org/pediatrics/view/journals/j-neurosurg-pediatr/28/1/article-p34.xml): "MRI-guided stereotactic placement of the infusion catheter (Brainlab Flexible Catheter) was performed … using an MRI-compatible system (ClearPoint Neuro, Inc.)." The infusion itself ran outside the MRI.
- **Not found:** any Brainlab-designed CED cannula that has its own clearance.

## Renishaw
- **neuroinfuse** is an intraparenchymal drug delivery system.
  - Renishaw flyer: https://www.renishaw.com/resourcecentre/download/flyer-neuroinfuse-intraparenchymal-drug-delivery-system--100797
  - CDNF release: https://www.renishaw.com/en/45590.aspx
- **What Renishaw says about it:**
  - It has a recessed-step catheter (guide tubes plus catheter) "to reduce backflow."
  - It has a "3D printed titanium transcutaneous port to allow the patient to remain in the MRI scanner during infusions."
  - "Drug-filled infusion lines are connected using an MRI compatible application set."
  - Renishaw describes the system as facilitating "convection enhanced delivery (CED) and other infusion applications."
- **Status:** "can only be used in the setting of an approved clinical trial." There is no commercial clearance.
- **Clinical use:**
  - The Bristol GDNF trial (Whone et al., Brain 2019, https://pmc.ncbi.nlm.nih.gov/articles/PMC6391602/) used "robot-assisted surgery for stereotactic implantation of the customized in-house CED system." The trial reports "a lack of commercially-available drug delivery devices" for repeated infusions. MRI was used after implantation to check the gadolinium test infusion.
  - The Herantis CDNF trial also used neuroinfuse (Renishaw release above).
  - Placement was robot or frame-based. It was not real-time MRI-guided placement like ClearPoint's.

## Devices named in the Parkinson's programs in our model
| Program | Delivery device named | Source |
|---|---|---|
| Bemdaneprocel Phase 1 (NCT04802733) | "a modified cannula (Smart Flow, Clearpoint Neuro)". Placement used a frameless MRI-guided approach in New York and a frame-based stereotactic approach in Toronto | Tabar et al., Nature 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC12095069/ |
| Bemdaneprocel exPDite-2 (NCT06944522) | No device named on ClinicalTrials.gov | https://clinicaltrials.gov/study/NCT06944522 |
| ANPD001 ASPIRO (NCT06344026) | ClearPoint Navigation System "for all patients," with the SmartFlow Cannula and Aspen Metered Delivery Syringe. The registry lists a "custom device … under MRI guidance" | Aspen, June 20, 2024, https://aspenneuroscience.com/parkinsons-disease-clinical-trial-uses-intraoperative-mri-to-guide-precision-implantation-of-patients-own-autologous-replacement-neurons/ ; https://clinicaltrials.gov/study/NCT06344026 |
| RNDP-001 (NCT07106021) | "Syringe Front-Loading Device." No navigation system or cannula named | https://clinicaltrials.gov/study/NCT07106021 |
| AB-1005 REGENERATE-PD (NCT06285643) and Phase 1b (NCT04167540) | "Bilateral image-guided infusion." No device named | https://clinicaltrials.gov/study/NCT06285643 |
| AAV2-GDNF NIH Phase 1 (NCT01621581) | CED with real-time intraoperative MRI (Heiss et al., Mov Disord 2019; Mol Ther 2022). I did not confirm the cannula's name from the paper text | https://escholarship.org/content/qt3vk5q95x/qt3vk5q95x.pdf |

## Verdict: partly supported
- **Brainlab: supported in substance.** I found no Brainlab-designed MRI-compatible CED cannula. Brainlab sells planning and navigation for catheter placement. The one Brainlab-branded catheter used for CED under MRI is listed under ClearPoint's (MRI Interventions') own 510(k).
- **Renishaw: contradicted on the letter.** Renishaw has a CED catheter system (neuroinfuse) with MRI-compatible parts. Patients can stay in the scanner during infusions. It is investigational and available only in clinical trials, and it is placed by robot or frame, not under real-time MRI.
- **The 10-K sentence is broadly accurate, but loose.** "Navigational platforms and cannulas useful for drug delivery under MRI" fits Brainlab (platforms, planning software, a ClearPoint-derived catheter) and Renishaw (an investigational CED catheter system with MRI-compatible components). Neither company has a commercially cleared, MRI-guided CED cannula of its own design that I could find.
- **Trial evidence:** every Parkinson's program that names a device uses ClearPoint's SmartFlow (bemdaneprocel Phase 1, ANPD001). One bemdaneprocel site placed the cannula frame-based without the ClearPoint platform, so ClearPoint's navigation system isn't required even where its cannula is used.
- **Not confirmed:** devices for exPDite-2, REGENERATE-PD and RNDP-001; whether ClearPoint manufactures the Brainlab catheter; and the device used in the AAV2-GDNF Phase 1.

## Update, Oct 25, 2026 (11:20 AM EDT)
- K123605 indication, checked in the FDA PDF: "The SmartFlow Flex Ventricular Catheter is intended for injection of Cytarabine or removal of CSF from the ventricles during intracranial procedures." Product code HCA. The 2021 DIPG study's brain-stem infusion falls outside this indication.
- Neurochase has agreed to buy Renishaw's neuroinfuse and all of its IP (announced Nov 20, 2025; transfers due by Jan 2026). It planned a DIPG trial for early 2026 and reports past humanitarian-approval use in children. https://neurochase.com/Blog/neurochase-announces-acquisition-of-strategic-renishaw-neuro-solutions-assets/
- Searched Oct 25, 2026: no confirmation found that the trial has started, and no regulatory clearance found. The Neurochase home page says nFuse is "Currently For investigational use only. Not approved for clinical use in any geography" (https://neurochase.com/). An ASGCT 2026 poster post says nFuse is "designed to be compatible with existing neurosurgical robots and frames".
- David's reasoning: nobody will risk a multi-billion-dollar therapy on a cannula that wasn't used in the trial.
