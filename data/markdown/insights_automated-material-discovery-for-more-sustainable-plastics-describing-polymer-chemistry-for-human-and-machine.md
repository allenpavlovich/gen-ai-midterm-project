---
title: Automated Material Discovery for More Sustainable Plastics: Describing Polymer Chemistry for Human and Machine – DSI
original_url: https://datascience.uchicago.edu/insights/automated-material-discovery-for-more-sustainable-plastics-describing-polymer-chemistry-for-human-and-machine
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogFeb 22, 2024

# Automated Material Discovery for More Sustainable Plastics: Describing Polymer Chemistry for Human and Machine

Ludwig Schneider, Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

!

Plastics are a double-edged sword for our environment. Every year, about [500 million tons](https://www1.compareyourcountry.org/global-plastics-outlook/en/0/all/default/all/OECD) of plastic are produced, most of which originate from petrochemical sources and end up as waste. Not only does this immense volume of plastic not decompose for centuries, but it also frequently escapes proper disposal, leading to environmental pollution. A stark example is the [Great Pacific Garbage Patch](https://en.wikipedia.org/wiki/Great_Pacific_garbage_patch), a massive accumulation of plastic in the Pacific Ocean. To put this pollution in perspective, if this patch were made entirely of typical 10-gram shopping bags, it would amount to approximately 10 billion bags, exceeding the human population on Earth.

However, it’s crucial to recognize that not all plastics are inherently harmful. They are incredibly versatile and economical, finding use in everything from everyday clothing and packaging to essential roles in micro-electronics, medical devices, and even battery electrolytes. Our goal, therefore, isn’t to eliminate plastics altogether but to explore sustainable alternatives and rethink our reliance on single-use items.

##### Sustainable Solutions

The path forward involves making plastics more sustainable. This could be achieved by using plant-based materials, ensuring compostability, or improving recyclability. Significant scientific progress has been made in developing such materials. However, the challenge doesn’t end with sustainability; these new materials must also functionally outperform their predecessors. A notable example is the case of [Sunchips’ compostable bags](https://zerowastesonoma.gov/news/sunchips-failed-noisy-compostable-packaging-gets-the-last-laugh), which, despite being environmentally friendly, were rejected by consumers due to their loud crinkling sound. This illustrates the need for sustainable plastics to meet both environmental and functional standards.

To address this challenge, science is rapidly advancing in the exploration of new materials through automated experimentation, computer simulations, and machine learning. However, these methods require a universal language to describe polymeric materials understandable to both computers and human scientists.

This brings us to the core of what makes plastics unique: polymers. Derived from the Greek words ‘πολύς’ (many) and ‘μέρος’ (parts), polymers are long molecules composed of repeating units called monomers. For instance, simplified [polyethylene](https://en.wikipedia.org/wiki/Polyethylene), the material of common shopping bags, is essentially a long chain of carbon atoms.

Visualizing the structure of a polymer like polyethylene can be straightforward for someone with a chemistry background. A basic representation using text characters, with dashes indicating [covalent](https://en.wikipedia.org/wiki/Covalent_bond) bonds between carbon (C) and hydrogen (H) atoms, looks like this:

!

This representation, while instructive for humans, poses a challenge for computers, especially due to its two-dimensional nature. By simplifying the notation and assuming implicit hydrogen bonds, we can transform it into a one-dimensional string more comprehensible to computers:

CCC….CCC

##### From SMILES Notation to BigSMILES

Expanding this concept leads us to [SMILES (Simplified Molecular Input Line Entry System)](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system), a widely-used notation for small molecules. However, traditional SMILES doesn’t address the varying lengths of polymers, as a real polymer chain consists of thousands of carbon atoms. Writing them all out would be impractical and overwhelming.

This challenge is elegantly solved by a notation specifically designed for polymers, known as [BigSMILES](https://olsenlabmit.github.io/BigSMILES/). It represents the repeating nature of monomers in a compact and understandable form. For instance, a simplified version of polyethylene can be represented as:

{[] [$]CC[$] []}

This format not only makes it easier for humans and machines to interpret but also allows for more detailed specification of connections and types of monomers, reflecting a wide range of realistic polymeric materials.

##### Representing Molecular Weight Distribution

One crucial aspect not yet addressed is the variation in the length of polymer chains in a material, known as the [molecular weight distribution](https://en.wikipedia.org/wiki/Molar_mass_distribution). This is where the generative version of BigSMILES, G-BigSMILES, comes into play. It allows the specification of molecular weight distributions, as demonstrated in the following example:

{[] [$]CC[$] []}|schulz\_zimm(5000, 4500)|

Here, the [Schulz-Zimm distribution](https://en.wikipedia.org/wiki/Schulz%E2%80%93Zimm_distribution) is used to describe the average chain lengths in terms of [molar masses](https://en.wikipedia.org/wiki/Molar_mass) (M\_w and M\_n). Here the molar mass is a description of how long the polymer chains are i.e. how many monomers are repeated to compose the chain molecule.

##### Closing the Loop: From Notation to Material Exploration

With G-BigSMILES, we can now comprehensively describe polymeric materials in a way that’s both human-readable and machine-processable. Our Python implementation allows for the generation of molecular models based on these descriptions, facilitating the exploration of material properties through computer simulations.

Real-world polymeric materials are often more complex, involving branched chains or multiple monomer types. For more in-depth examples, readers are encouraged to consult our [publication](https://doi.org/10.1039/D3DD00147D) and [GitHub repository](https://github.com/InnocentBug/bigSMILESgen).

##### Looking Ahead: AI-Driven Material Discovery

The next step in our project involves enhancing the interpretability of G-BigSMILES for machines. By translating these notations into graph structures, we aim to enable AI algorithms to suggest new material compositions. The goal is to ensure that these suggestions are not only chemically valid but also optimized for performance, paving the way for more efficient and sustainable material discovery.

---

*This work was *supported* by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Program of Schmidt Futures.*

!

Related

Research

* [Research Initiative

  ## AI + Science](https://datascience.uchicago.edu/research/ai-science/)

Insights

* [BlogFeb 15, 2024

  ## Unlocking the Potential of Lithium Batteries with New Electrolyte Solutions](https://datascience.uchicago.edu/insights/unlocking-the-potential-of-lithium-batteries-with-new-electrolyte-solutions/)

News

* [Campus NewsOct 26, 2022

  ## New Schmidt Futures Fellowship at UChicago to Foster Next Generation of AI-Driven Scientists](https://datascience.uchicago.edu/news/new-schmidt-futures-fellowship-at-uchicago-to-foster-next-generation-of-ai-driven-scientists/)
* [DSI NewsMay 22, 2024

  ## Eric and Wendy Schmidt AI in Science Postdoctoral Fellows host first-ever hackathon](https://datascience.uchicago.edu/news/eric-and-wendy-schmidt-ai-in-science-postdoctoral-fellows-host-first-ever-hackathon/)