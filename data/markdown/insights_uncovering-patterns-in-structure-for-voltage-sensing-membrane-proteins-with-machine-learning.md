---
title: Uncovering Patterns in Structure for Voltage Sensing Membrane Proteins with Machine Learning – DSI
original_url: https://datascience.uchicago.edu/insights/uncovering-patterns-in-structure-for-voltage-sensing-membrane-proteins-with-machine-learning
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogApr 18, 2024

# Uncovering Patterns in Structure for Voltage Sensing Membrane Proteins with Machine Learning

Aditya Nandy, Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

How do organisms react to external stimuli? The molecular details of this puzzle remain unsolved.

Humans, in particular, are multi-scale organisms. Various biological systems (i.e. the respiratory system, digestive system, cardiovascular system, endocrine system, etc.) comprise the human body. Within each of these systems, there are organs, which are made of tissues. Each tissue is then made of cells. Within cells, there are smaller pieces of machinery known as organelles. Cells and organelles are composed of a variety of proteins and lipids. In particular, proteins that are embedded in lipids (as opposed to floating within the cell) are known as membrane proteins.

Although there are clear differences between organisms (i.e. bacteria, humans, and mice) at the cellular and atomic scales, the protein machinery looks very similar. Indeed, challenges in predicting protein structure led to the breakthrough of [AlphaFold](https://www.nature.com/articles/s41586-021-03819-2), enabling scientists to make [predictions](https://alphafold.ebi.ac.uk/) on protein structure given a primary sequence of amino acids (the building blocks of proteins). Cells and organelles across different organisms sense stimuli such as touch, heat, and voltage with a specific type of protein called a membrane protein. These membrane proteins are usually embedded on the membrane that defines the “inside” and “outside” of a cell or an organelle, and thus are responsible for sensing. Despite advances in protein structure prediction with AlphaFold, challenges remain for predicting the structures of membrane proteins. We can utilize existing experimental structures, however, to try and decipher patterns for voltage sensing.

#### **Voltage Sensing Proteins**

Voltage sensing membrane proteins are specialized molecular entities found in the cell membranes of various organisms, ranging from bacteria to humans. These remarkable proteins play a pivotal role in cellular function by detecting and responding to changes in the electrical potential across the cell membrane. Through their sophisticated structure and mechanisms, voltage sensing membrane proteins enable cells to perceive, process, and transmit electrical signals essential for vital physiological processes such as neuronal communication (i.e. passing action potentials), muscle contraction, and cardiac rhythm regulation. For instance, neurons have voltage-gated ion channels – channels that open and allow the flux of ions into the cell to produce electrical signals.

Despite the complexity of voltage sensing proteins that are able to sense different voltages with high sensitivity, the biology of voltage sensors is highly modular. Proteins that respond to voltage typically have what is known as a “voltage sensing domain,” or VSD. The VSD is usually coupled to a larger module that is responsible for function. For instance, in a voltage-gated ion channel, the ion channel itself is coupled to one or more VSDs that enable it to behave in a voltage-sensitive way. The modular nature of the VSD, which is nearly always a 4-helix bundle, enables comparison across VSDs from different proteins (and organisms!) using machine learning. Over the full protein data bank (PDB) where protein structures are deposited by experimental structural biologists, we can extract thousands of VSDs from various proteins.

!

Figure 1. A typical voltage sensor (left) for a membrane protein (right) that has multiple voltage sensing domains.

#### **Analogy to Modified NIST (MNIST) Digit Dataset**

At its root, we would like to determine any patterns between voltage sensors that may have similar function, turning the problem into one of “pattern recognition” that can be tackled with machine learning. Analogous pattern recognition problems have been carried out by computer scientists for decades. The MNIST data set is a classic task in machine learning for classifying hand-written digits. The key concept in classifying MNIST digits is that each digit has a set of characteristics, or “features,” that underlies its membership to a certain label (in this case, 1 through 9). Humans can identify these digits, but a machine learning model must pick out the key similarities and differences between these digits to separate them.

!

Figure 2. Digits from MNIST (left, figure adapted from Wikipedia). Digits are hand-written. Each row represents a category of digits.

In a similar vein, VSDs must have underlying features and characteristics that make them uniquely sensitive to different voltages. One key difference that makes working with scientific data more challenging than MNIST is that we do not always have labels. Or more specifically, we do not know the sensitivity of the voltage sensor unless a functional study has been carried out.

#### **The Excitement**

Using machine learning to fingerprint and cluster VSDs represents an opportunity to move beyond sequence-to-structure prediction, like AlphaFold, and on to structure-to-function analysis. Through analyses on structural similarities and differences, we may be able to discern the molecular basis for voltage sensitivity and the key structural features that are essential for a protein to respond to voltage. Understanding this response to voltage can help us understand how the molecular machinery of the body behaves under native and diseased conditions.

Together with the [Vaikuntanathan](https://vaikuntanathan-group.uchicago.edu/), [Roux](https://chemistry.uchicago.edu/faculty/beno%C3%AEt-roux), and [Perozo](https://www.nasonline.org/member-directory/members/20056778.html) laboratories and the newly formed Center for Mechanical Excitability at the University of Chicago, I continue to investigate voltage-sensitive proteins to understand how they underlie how cells respond to stimuli.

*This work was supported by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Program of Schmidt Futures.*

Related

Research

* [Research Initiative

  ## AI + Science](https://datascience.uchicago.edu/research/ai-science/)

Insights

* [BlogApr 11, 2024

  ## Finding the likely causes when potential explanatory factors look alike](https://datascience.uchicago.edu/insights/finding-the-likely-causes-when-potential-explanatory-factors-look-alike/)
* [BlogApr 04, 2024

  ## An Intro to Gravitational-Wave Astronomy](https://datascience.uchicago.edu/insights/an-intro-to-gravitational-wave-astronomy/)
* [BlogApr 25, 2024

  ## Towards New Physics at Future Colliders: Machine Learning Optimized Detector and Accelerator Design](https://datascience.uchicago.edu/insights/towards-new-physics-at-future-colliders-machine-learning-optimized-detector-and-accelerator-design/)
* [BlogMay 02, 2024

  ## From Protein Structures to Clean Energy Materials to Cancer Therapies: Using AI to Understand and Exploit X-ray Damage Effects](https://datascience.uchicago.edu/insights/from-protein-structures-to-clean-energy-materials-to-cancer-therapies-using-ai-to-understand-and-exploit-x-ray-damage-effects/)

+ Show All
- Show Less

## More on this topic

[!

BlogFeb 26, 2025

## Federal budget cuts threaten to decimate America’s AI superiority—and other countries are watching](https://datascience.uchicago.edu/insights/federal-budget-cuts-threaten-to-decimate-americas-ai-superiority-and-other-countries-are-watching/)
[![A video frame example from Cityscape dataset where different colors denote different labels in pixel level. For example, red means person and light blue means sky.](https://datascience.uchicago.edu/wp-content/uploads/2024/05/cityscape-750x500.png)

[Image: A video frame example from Cityscape dataset where different colors denote different labels in pixel level. For example, red means person and light blue means sky.]

BlogJun 06, 2024

## Behind Automatic Video Semantic Segmentation](https://datascience.uchicago.edu/insights/behind-automatic-video-semantic-segmentation/)
[![Microbial organisms drive the carbon cycle. Image adapted from Wu et al. 2024 https://doi.org/10.1016/j.scitotenv.2023.168627](https://datascience.uchicago.edu/wp-content/uploads/2024/05/Carbon_cycle-750x500.jpg)

[Image: Microbial organisms drive the carbon cycle. Image adapted from Wu et al. 2024 https://doi.org/10.1016/j.scitotenv.2023.168627]

BlogMay 30, 2024

## Searching for simplicity in microbial communities](https://datascience.uchicago.edu/insights/searching-for-simplicity-in-microbial-communities/)
[![Fig: Formation of HIV capsid simulated by a coarse-grained model.
From: https://www.google.com/url?q=https://www.science.org/doi/epdf/10.1126/sciadv.add7434&sa=D&source=docs&ust=1715014663521469&usg=AOvVaw3fATTBC_yAvxPv6WPYI17_](https://datascience.uchicago.edu/wp-content/uploads/2024/05/HIV-capsid-750x500.png)

[Image: Fig: Formation of HIV capsid simulated by a coarse-grained model.
From: https://www.google.com/url?q=https://www.science.org/doi/epdf/10.1126/sciadv.add7434&sa=D&source=docs&ust=1715014663521469&usg=AOvVaw3fATTBC\_yAvxPv6WPYI17\_]

BlogMay 22, 2024

## AI as a Great Teacher for Molecular Dynamic Modeling](https://datascience.uchicago.edu/insights/ai-as-a-great-teacher-for-molecular-dynamic-modeling/)