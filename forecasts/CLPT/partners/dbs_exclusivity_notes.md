# DBS and PD cell/gene therapy: exclusivity evidence (research notes, 25 Oct 2026)
Read-only research. No model numbers changed. Criteria text from the ClinicalTrials.gov API v2 (full criteria fields read). Publications read as abstracts/search snippets only.

| Trial | Prior DBS excluded? | Quoted text | Link |
|---|---|---|---|
| Bemdaneprocel exPDite-2 (Ph3) | Yes | "Prior surgical or radiation therapy to the brain, including deep brain stimulation (DBS) and lesion therapy..." | https://clinicaltrials.gov/study/NCT06944522 |
| AB-1005 REGENERATE-PD (Ph2) | Yes | "Prior history of brain surgery including, but no limited: DBS, pallidotomy focused ultrasound thalamotomy..." | https://clinicaltrials.gov/study/NCT06285643 |
| AB-1005 Japan | Yes | same text | https://clinicaltrials.gov/study/NCT07566429 |
| AAV2-GDNF Ph1 (NIH/AskBio) | Yes | "Prior brain surgery, including GDNF, NTN, GAD, AADC therapy or deep brain stimulation." | https://clinicaltrials.gov/study/NCT01621581 |
| AAV2-GDNF Ph1b (NCT04167540) | Yes | "Prior brain surgery (i.e. deep brain stimulator or DBS implantation)..." | https://clinicaltrials.gov/study/NCT04167540 |
| ANPD001 ASPIRO (Ph1/2a) | Yes | "History of intracranial therapy for PD, including deep brain stimulation (DBS), focused ultrasound (FUS), gene therapy or other biological therapy" | https://clinicaltrials.gov/study/NCT06344026 |
| RNDP-001 (Kenai) | Yes (implicit) | "Previous infusion therapy or surgery for Parkinson's disease" | https://clinicaltrials.gov/study/NCT07106021 |
| VY-AADC01 Ph1 | Yes + DBS deferred 12 mo | "Prior brain surgery including deep brain stimulation..."; "agrees to defer any neurological surgery, including deep brain stimulation, until after completing the 12 month study visit" | https://clinicaltrials.gov/study/NCT01973543 |
| VY-AADC02 RESTORE-1 | Yes (judgment-based) + DBS deferred | "Prior brain surgery... that could complicate the study procedure or negatively impact study evaluations"; agree to defer DBS "until after the study is completed, if medically appropriate" | https://clinicaltrials.gov/study/NCT03562494 |
| CERE-120 (AAV2-neurturin) Ph1/2 | Yes + DBS deferred | "Any prior treatment for PD with a procedure involving intracranial surgery or implantation of a device (e.g. DBS, pallidotomy)"; not to undergo DBS for 12 months / while blinded | https://clinicaltrials.gov/study/NCT00985517 |

Not checked: Tabar et al. Nature 2025 Ph1 (exPDite) criteria, AAV-GAD, fetal-transplant trial (Freed 2001/Olanow 2003) entry criteria.

Stated reasons: no registry entry gives a reason. The RESTORE-1 wording (would "complicate the study procedure or negatively impact study evaluations") and the DBS deferral clauses point to confounding of the efficacy readout and surgical complexity. No trial cites a biological contraindication. (This is my inference.)

## Reverse direction: DBS after a graft (published)
- Herzog et al., Mov Disord 2008: 2 fetal-graft patients got GPi/STN DBS; both improved. https://pubmed.ncbi.nlm.nih.gov/18536037/ (abstract)
- Graff-Radford et al., Arch Neurol 2006: GPi DBS resolved runaway dyskinesia 11 years after a graft. https://jamanetwork.com/journals/jamaneurology/fullarticle/791926 (abstract/snippet)
- Freed group, npj Parkinson's Dis 2021: 3 of 34 graft recipients got pallidal stimulators for graft-induced dyskinesia; these improved. https://www.nature.com/articles/s41531-021-00183-w (abstract)

## Graft in patients with existing DBS / combining the two
- MDS abstract (Kentucky group, Schwann-cell nerve graft): 3 patients with an existing STN lead had GPi DBS plus putaminal and nigral grafts; adverse events "comparable to standard DBS surgery"; perioperative MRI was unremarkable. https://www.mdsabstracts.org/abstract/unilateral-delivery-of-cell-based-therapy-to-the-putamen-and-substantia-nigra-in-patients-with-parkinsons-disease-who-have-an-existing-dbs-system/ (abstract)
- Expert opinion, Mov Disord 2015 ("Combining cell transplants or gene therapy with DBS"): proposes delivering biologics at the time of DBS implantation and suggests combination strategies. https://doi.org/10.1002/mds.26083 (abstract)

## Practical constraints (evidence vs opinion)
- Most current DBS systems are MR-conditional, but under restricted conditions (often 1.5T and limited SAR). AB-1005, VY-AADC and AAV2-GDNF all use real-time intraoperative MRI with gadoteridol (PMC6593762; Mol Ther 2022). My view, not verified this turn: an implanted lead may limit iMRI sequences and cause artifacts, and the stated reasons for exclusion are confounding and complexity. Lead targets (STN/GPi) differ from the putaminal graft target, but the frontal trajectories could come close to each other. I found no study measuring this.
- I found no FDA, BlueRock, Bayer or Aspen statement on whether these therapies complement or replace DBS. No label exists yet.

## Read
Exclusivity is supported as a trial-entry rule, since every trial excludes prior DBS. It is not supported as a biological or label rule. DBS after a graft is documented (small case series), and grafting with DBS already in place has been done in 3 patients. Labels for devices and surgical biologics usually don't carry trial-entry exclusions (for example, the Medtronic label has no age cap), but I found no evidence about the future label.

Model suggestion:
- Base: keep the 42k already-DBS patients in the eligible pool, with an optional modest haircut for practical friction. Keep counting DBS procedures in the shared treated total, because each patient still chooses one procedure per year of decision. Don't treat DBS as removing patients from the pool permanently.
- Bear: use trial-style exclusion (remove prior-DBS patients from the pool).
- Upside: sequential use (graft, then DBS for residual symptoms or graft-induced dyskinesia) adds ClearPoint procedures. It is not modelled.
