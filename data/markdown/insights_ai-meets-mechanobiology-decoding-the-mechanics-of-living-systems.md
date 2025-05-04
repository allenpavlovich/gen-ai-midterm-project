---
title: AI Meets Mechanobiology: Decoding the Mechanics of Living Systems – DSI
original_url: https://datascience.uchicago.edu/insights/ai-meets-mechanobiology-decoding-the-mechanics-of-living-systems
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogJul 30, 2024

# AI Meets Mechanobiology: Decoding the Mechanics of Living Systems

Shailaja Seetharaman, Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

Mechanical forces are everywhere. From blood flow through arteries to pressure in the airways, and we are continuously sensing and responding to such varying stimuli. Whether it is a single cell sensing its local microenvironment or us as a whole reacting to external stimuli, forces orchestrate form and function. For example, shear stress in blood vessels is crucial for cardiovascular health, while in cancer, extracellular matrix stiffness affects tumor growth and metastasis. However, the mechanisms by which mechanical cues orchestrate tissue functions remain elusive. Introducing new approaches from artificial intelligence (AI) and machine learning (ML) with domain knowledge in biology, we can decode the mechanics of biological systems.

!

Figure 1. Endothelial tissue in response to changes in shear stress. Microscopy image of human aortic endothelial cells experiencing disturbed flow mimicking atherosclerosis in arteries. Cells are stained for actin (magenta), cell junctions/boundaries using VE-Cadherin (red), and a mechanosensitive protein called Four-and-a-half LIM domain protein 2 (FHL2; cyan).

**Challenges in Biological Systems**

When cells and tissues respond to forces, several events occur in parallel. Proteins move around within the cell, alter their interactions and signaling, resulting in drastic remodeling of subcellular structures like the nucleus and [cytoskeleton](https://www.sciencedirect.com/science/article/abs/pii/S0962892420301227). Some structures assemble and grow, while others disassemble. These molecular and subcellular events drive tissue-scale behaviors, leading to phenomena such as [cell shape changes, cell adhesion and migration](https://www.nature.com/articles/nrm2957). Compared to physical systems where theoretical modeling has been very successful, engineering models for living systems are still a nascent stage. 

Living systems are made up of thousands of different biological molecules that function with highly dynamic and non-linear interactions. Fundamentally, this means that our current modeling approaches and engineering disciplines that rely on studies of non-living systems will be inapplicable in biology. Furthermore, several AI “blackbox” models lack interpretability, and this is a critical problem, particularly when used to predict diseased states or patient health. Despite these challenges, AI holds immense potential in decoding vast biological data. AI algorithms can analyze large genomics/proteomics datasets and microscopy images to identify patterns and correlations, helping us develop targeted therapies to enhance precision medicine.

**Harnessing AI in Cardiovascular Research**

Understanding how [force sensing and adaptation](https://www.annualreviews.org/content/journals/10.1146/annurev-bioeng-092419-060810) occurs in cardiovascular systems is an extremely important step towards identifying and designing targeted therapies for heart diseases. Inspired by the successes of AI in [protein structure and interactions](https://alphafold.ebi.ac.uk/), drug design and digital pathology, researchers are exploring the potential of AI in mechanobiology. For example, machine learning models can detect subtle changes in signals that could indicate heart failure or atrial fibrillation. 

As a Schmidt AI in Science Postdoctoral Fellow, I’ve been interested in exploiting AI/ML approaches in addressing one of the open problems in the field of vascular mechanobiology, namely, how [blood flow variations in diseases](https://journals.physiology.org/doi/full/10.1152/ajpcell.00449.2022) like atherosclerosis impact tissue phenotypes and functions. Specifically, we are predicting how cardiac endothelial cells respond to laminar blood flow in healthy arteries or turbulent flow seen in diseases like atherosclerosis. Using machine learning tools and high-throughput methods to model how proteins, subcellular structures, and tissues behave in response to force perturbations, we hope to unravel how mechanotransduction impacts cardiovascular health and disease.

**Neural Networks in Mechanobiology**

Neural network architectures like convolutional neural networks (CNNs) and graph neural networks (GNNs) are currently used for predicting biological phenomena. CNNs, specifically, [U-Nets](https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28), are highly effective in analyzing image datasets, and can be used to predict how subcellular structures, cell morphologies, and tissue architectures depend on mechanical forces. Such methods can be exploited to accurately predict whether tissues are healthy or diseased, and forecast disease progression. For instance, using U-Nets, we are extracting features from high-resolution microscopy images of cardiac endothelial cells, aiming to detect and identify regions of the tissue where diseased phenotypes are evident. Such machine learning models can help elucidate how specific perturbations or mechanical forces influence tissue behavior and will advance our abilities to decipher the mechanisms of cardiovascular disease progression.

GNNs are also widely used to model complex interactions within biological networks. By representing these [interactions as graphs](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9481156/), GNNs capture how mechanical forces propagate through tissues and influence cellular functions. This is particularly useful in studying mechanotransduction, where mechanical signals are converted into biochemical responses. GNNs can help decode mechanochemical pathways through which forces lead to cell and tissue behaviors, providing insights into disease mechanisms.

!

Figure 2. Summary of AI/ML approaches in cell and tissue mechanobiology, using endothelial flow response as an example.

My work demonstrates neural networks can be used to forecast subcellular and tissue dynamics and to engineer model tissues to combat diseases. AI/ML tools can also predict the extent of disease progression, aid in drug design, and allow the translation of fundamental biological phenomena into clinical settings.

*This work was supported by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Program of Schmidt Sciences.*

!