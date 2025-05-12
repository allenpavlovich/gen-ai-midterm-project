---
title: Marie-Laure Charpignon – DSI
original_url: https://datascience.uchicago.edu/people/marie-laure-charpignon
category: people
date: 2025-05-04
---

<!-- Table-like structure detected -->

!

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

People / Non-DSI

# Marie-Laure Charpignon

PhD Candidate, Massachusetts Institute of Technology

**Bio:** Marie is a PhD candidate at MIT Institute for Data, Systems, and Society, conducting research at the Laboratory for Information and Decision Systems and the Broad Institute. Her research combines statistical machine learning, causal inference, and network science, with applications in medicine and public health.

In particular, she builds disease-specific hypergraphs to formulate drug repurposing hypotheses and utilizes the target trial emulation framework to evaluate repurposing candidates for Alzheimer’s disease and related dementias using structured (e.g., diagnosis codes) and unstructured data (e.g., clinical notes) from electronic health records, across multiple medical centers. Methodologically, her work involves the use of doubly-robust machine learning and causal matrix estimation and the development of synthetic control and instrumental variable approaches adapted to survival analysis. With a focus on aging populations, she also designs comprehensive agent-based models that integrate granular sociodemographic and mobility data to optimize the distribution of vaccines against infectious diseases at the state and national level and inform public policy decision-making.

Previously, Marie obtained a BSc in Engineering Sciences from Ecole Centrale Paris in France and a MSc in Computational and Mathematical Engineering from Stanford University. As a data scientist at Microsoft, she analyzed the effects of technology usage and digital collaboration on student academic outcomes and socio-emotional learnings in school networks with treatment spillovers. She interned at Goldman Sachs, Microsoft Research, the European Commission, INSERM-INRIA in France, and Clalit Innovation in Israel.

**Talk Title:** Antihypertensive drug repurposing for dementia prevention: target trial emulations in two large-scale electronic health record systems

**Abstract:** Alzheimer’s disease (AD)—the most common type of dementia—affects 5.7 million people in the US and costs about $250 billion annually. Since there are no disease-modifying therapies to date, repurposing FDA-approved drugs preventing dementia onset offers an expedited path to reduce the impact of this epidemic. Beyond age, type 2 diabetes and hypertension are two major risk factors for dementia onset. However, mixed results are emerging from prior observational studies contrasting various antihypertensive drug classes, including Angiotensin Converting Enzyme (ACE) inhibitors, Angiotensin Receptor Blockers (ARB), and Calcium Channel Blockers (CCB).

To address this complexity and evaluate the repurposing potential of antihypertensives with different mechanisms of action, we deployed a causal inference approach accounting for the competing risk of death in emulated clinical trials using two distinct electronic health record (EHR) systems, one from the UK Clinical Research Practice Datalink (CPRD) and the other from the US Research Patient Data Registry (RPDR). We performed intention-to-treat analyses among patients aged 50 or older at baseline, applying Inverse Propensity score of Treatment Weighting to balance the two treatment arms with respect to a set of confounders curated by cardiologists and neurologists. Specifically, we compared antihypertensive treatment initiation with any of seven ARBs vs any of eleven ACE inhibitors.

In the US RPDR database, a total of 45,206 patients were eligible to participate in the emulated target trial. Treatment initiation with any of the seven ARBs was associated with lower hazard of all-cause mortality (HR=1.16 [95% CI: 1.10-1.23]) and lower cause-specific hazard of dementia onset (HR=1.34 [95% CI: 1.27-1.42]) in cause-specific Cox Proportional Hazards (PH) models, after accounting for prolonged survival, relative to treatment initiation with any of the eleven ACE inhibitors. In addition, within the ARB drug class, the gap in the dementia risk difference over time was more pronounced among patients initiating on compounds that cross the blood-brain barrier (BBB). Results of the competing risks analysis were robust to the structure of the outcome models (i.e., Cox PH vs nonparametric). The directionality and strength of our findings were similar in the UK CPRD database.

Target trial emulations in two large-scale EHR systems suggest that treatment initiation with BBB-crossing ARBs might reduce the risk of dementia among hypertensive patients. Ongoing work includes the conduct of a mediation analysis in the two considered cohorts to assess the role played by enhanced blood pressure control towards dementia prevention.

Contact Info

Website

<https://dahleh.lids.mit.edu/teams/marie-laure-charpignon/>