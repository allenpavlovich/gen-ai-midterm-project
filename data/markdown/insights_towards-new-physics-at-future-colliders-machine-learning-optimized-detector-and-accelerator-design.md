---
title: Towards New Physics at Future Colliders: Machine Learning Optimized Detector and Accelerator Design – DSI
original_url: https://datascience.uchicago.edu/insights/towards-new-physics-at-future-colliders-machine-learning-optimized-detector-and-accelerator-design
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogApr 25, 2024

# Towards New Physics at Future Colliders: Machine Learning Optimized Detector and Accelerator Design

Anthony Badea, Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

We are in an exciting and challenging era of fundamental physics. Following the discovery of the  Higgs boson at CERN’s Large Hadron Collider (LHC), there have been 10 years of searches for new physics without discovery. The LHC, shown below, collides protons at nearly the speed of light to convert large quantities of energy to exotic forms of matter via the energy-mass relationship E=mc2. The goal of our searches is to discover new particles which could answer some of the universe’s most fundamental questions. What role does the Higgs play in the origin and evolution of the Universe? What is the nature of dark matter? Why is there more matter than antimatter in the universe? Given the absence of new particles, the field is devising new methods, technologies, and theories. Some of the most exciting work is towards building more powerful colliders. In this work, an emerging theme is the use of machine learning  (ML) to guide detector and accelerator designs.

!

Figure 1: Aerial view of the 27-kilometer-long Large Hadron Collider (LHC) located on the border of France and Switzerland near Geneva. The LHC collides particles at nearly the speed of light to study the universe in a controlled experimental facility. The Higgs boson was discovered with the LHC in 2012. [Image credit to ESO Supernova.](https://supernova.eso.org/exhibition/images/cern-aerial-cc/)

The goal of building new colliders is to precisely measure known parameters and attempt to directly produce new particles. As of 2024, the most promising designs for future colliders are the [Future Circular Collider](https://fcc.web.cern.ch) (FCC), [Circular Electron Positron Collider](http://cepc.ihep.ac.cn/intro.html) (CEPC), [International Linear Collider](https://linearcollider.org) (ILC), and [Muon Collider](https://muoncollider.web.cern.ch/welcome-page-muon-collider-website) (MuC). The main difference between the proposals is the type of colliding particles (electrons/positrons, muons/anti-muons, protons-protons), the shape (circular/linear), the collision energy (hundreds vs. thousands of gigaelectronvolts), and the collider size (10 – 100 km). A comparison between the current LHC and proposed future colliders is shown below.

!

Figure 2: Size comparison between the current LHC and proposed future colliders: Muon Collider (red), LHC (light blue), International Linear Collider (green), and Very Large Hadron Collider (outmost light blue labeled as VLHC). Note the VLHC was a similar proposal but roughly twice as large as the Future Circular Collider. [Image credit Fermilab.](https://muoncollider.fnal.gov)

Designing the accelerator and detector complexes for future colliders is a challenging task. The design involves detailed simulations of theoretical models and particle interactions with matter. Often, these simulations are computationally expensive, which constrains the possible design space. There is ongoing work to overcome this computational challenge by applying advances in surrogate modeling and Bayesian optimization. Surrogate modeling is the technique for creating a fast approximate simulation of an expensive, slow simulation, increasingly using neural networks. Bayesian optimization is a technique to optimize black box functions without assuming any functional forms. The combination of these approaches can reduce computing expenses considerably.

An example of ML guided optimization is ongoing for one of the outstanding challenges for a MuC. A [MuC is an exciting future collider](https://www.science.org/content/article/muon-collider-could-revolutionize-particle-physics-if-it-can-be-built) proposal that would be able to reach high energies in a significantly smaller circumference ring than other options. To create this machine, we must produce, accelerate, and collide muons before they decay. A muon is a particle similar to the electron but around 200 times heavier. The most promising avenue for this monumental challenge starts by hitting a powerful proton beam on a fixed target to produce pions, which then decay into muons. The resulting cloud of muons is roughly the size of a basketball and needs to be cooled into a 25µm size beam within a few microseconds. Once cooled, the beam can be rapidly accelerated and brought to collide. The ability to produce compact muon beams is the missing technology for a muon collider. Previously proposed cooling methods did not meet physics needs and relied on ultra-powerful magnets beyond existing technology. There are alternative designs that could remedy the need for powerful magnets, but optimization of the designs is a significant hurdle to assessing their viability.

In a growing partnership between Fermilab and UChicago, we are studying how to optimize a muon-cooling device with hundreds of intertwined parameters. Each optimization step will require evaluating time and resource intensive simulations, constraining design possibilities. So, we are attempting to build surrogates of the cooling simulations and apply Bayesian optimization on the full design landscape. There have been [preliminary results](https://indico.cern.ch/event/1325963/contributions/5792978/attachments/2818799/4922076/FC_lattice_IMCC2024.pdf) by researchers in Europe that show this approach has potential, but more work is needed.

To make progress on this problem, we are starting simple – trying to reproduce previous results from classical optimization methods. Led by UChicago undergraduates Daniel Fu and Ryan Michaud, we are performing [bayesian optimization using gaussian processes](https://scikit-optimize.github.io/stable/modules/generated/skopt.gp_minimize.html). This does not include any neural networks but helps build our intuition for the optimization landscape and mechanics of the problem. The first step of this process is determining if the expensive simulation can be approximated by a gaussian process to produce a fast surrogate. If it can be then the optimization can proceed. If not then we’ll need to deploy a more complex model like a neural network. We hope to have preliminary results by the summer ‘24 and contribute to the upcoming [European strategy update for particle physics](https://europeanstrategy.cern).

*This work was supported by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Program of Schmidt Futures.*

Related

Research

* [Research Initiative

  ## AI + Science](https://datascience.uchicago.edu/research/ai-science/)

Insights

* [BlogApr 18, 2024

  ## Uncovering Patterns in Structure for Voltage Sensing Membrane Proteins with Machine Learning](https://datascience.uchicago.edu/insights/uncovering-patterns-in-structure-for-voltage-sensing-membrane-proteins-with-machine-learning/)
* [BlogApr 11, 2024

  ## Finding the likely causes when potential explanatory factors look alike](https://datascience.uchicago.edu/insights/finding-the-likely-causes-when-potential-explanatory-factors-look-alike/)
* [BlogMay 02, 2024

  ## From Protein Structures to Clean Energy Materials to Cancer Therapies: Using AI to Understand and Exploit X-ray Damage Effects](https://datascience.uchicago.edu/insights/from-protein-structures-to-clean-energy-materials-to-cancer-therapies-using-ai-to-understand-and-exploit-x-ray-damage-effects/)

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