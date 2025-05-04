---
title: Searching for simplicity in microbial communities – DSI
original_url: https://datascience.uchicago.edu/insights/searching-for-simplicity-in-microbial-communities
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogMay 30, 2024

# Searching for simplicity in microbial communities

Kyle Crocker, future Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

Global nutrient cycles both provide the basis for the food webs that support life on Earth and control the levels of greenhouse gasses such as carbon dioxide and nitrous oxide in Earth’s atmosphere. Underlying these cycles are chemical transformations, for instance from organic carbon to carbon dioxide and nitrate to nitrogen gas, that are driven by the metabolic activity of microbial organisms.

!

Microbial organisms drive the carbon cycle. Image adapted from Wu et al. 2024 <https://doi.org/10.1016/j.scitotenv.2023.168627>

My collaborators and I seek to understand the collective behavior of communities of these microbes. A key barrier to such an understanding is the complexity of these biological systems: for instance, each gram of soil can contain thousands of microbial strains. Each of these strains can, in principle, impact the activity of the other strains in the microbial community (microbial interactions) as well as contribute to the collective behavior of the community as whole (e.g., nutrient cycling). Additionally, microbial communities in the wild often reside in dynamic, spatially heterogeneous, and multi-dimensional environments. So how do we deal with this complexity?

Motivated by the fields of statistical physics and systems biology, which find that systems that are complex at the microscopic level often give rise to simple collective behavior at the macroscopic level, we hypothesize that similar *emergent simplicity* is present in microbial communities. Indeed, recent [theoretical](https://www.biorxiv.org/content/biorxiv/early/2024/03/29/2024.03.26.586882.full.pdf) and empirical studies have provided support for such a hypothesis, perhaps most influentially in a [paper published in Science in 2018](https://www.science.org/doi/10.1126/science.aat1168), which demonstrated a convergence in the composition of microbial communities extracted from 12 leaf and soil samples and assembled in controlled laboratory conditions. While this work undoubtedly represents a significant advance, it has [garnered criticism](https://x.com/NoahFierer/status/1779992564831076584) from microbial ecologists, who point out that such experiments, which remove microbes from their natural habitats and impose a strong selection pressure for particular traits, are not a good representation of the experience of microbes in the wild. To avoid this complication, studies in microbial ecology often consist of [genomic sequencing surveys](https://microbiologysociety.org/resource_library/knowledge-search/microbiome-beyond-the-gut.html), which sample microbial gene content from natural environments such as the [ocean](https://www.nature.com/articles/s41579-020-0364-5) and [topsoil](https://www.nature.com/articles/s41586-018-0386-6), often associating variation in gene content with environmental factors. However, it is not possible to make causal statements about the role of the environment or microbial interactions in structuring microbial ecosystems from observational studies alone. As a result, there is a major gap between what we can learn from controlled laboratory studies and observations in the field.

To bridge this gap, we have developed an approach that provides a tantalizing glimpse of simplicity in natural microbial communities. [Our approach](https://doi.org/10.1101/2023.05.31.542950) seeks to connect laboratory experiments to patterns observed in field studies. To do this, we first identified a simple pattern that couples the abundance of two genes involved in the nitrogen cycle to pH in a global topsoil microbiome survey dataset: as pH increases, the relative abundance of one [nitrate reductase](https://en.wikipedia.org/wiki/Nitrate_reductase#:~:text=Prokaryotic%20nitrate%20reductases%20have%20two,NAP%20cannot%20do%20so.) gene (*nap)* increases, while the relative abundance of another nitrate reductase gene (*nar)* decreases. To understand the origin of this pattern, we needed the ability to perform laboratory experiments on the microbes involved. We therefore sampled soil from the environment, extracted microbial communities, and grew them in different pH conditions in the lab. Strikingly, we found that the same gene to pH coupling observed in the global survey data was reproduced in the lab across six soil samples! This allowed us to isolate and characterize the microbes that drive this pattern, revealing a pH-modulated interaction between microbes with the relevant genes. Crucially, this interaction seems to be conserved *across microbial species,* giving rise to the simple pattern identified in the survey data.

!

pH modulates interactions. Strains with nar (blue) and nap (orange) genes coexist via nutrient exchange at acidic pH, whereas the nap strain out-competes the nar strain at neutral pH. Figure created with [BioRender.com](http://BioRender.com).

This finding raises an intriguing possibility: perhaps the activity of microbes is not species-dependent, but rather follows large-scale patterns that persist across many species. Is this phenomenon is a generic feature of natural microbial communities? To test this idea, we plan to subject intact soil samples to a suite of environmental perturbations and measure the response of both species abundances and community-level emission of carbon dioxide. Using machine learning tools such as [variational autoencoders](https://en.wikipedia.org/wiki/Variational_autoencoder#:~:text=A%20variational%20autoencoder%20is%20a,%26%20slab)%20sparse%20coding).), we hope to identify a simplified description of the community that connects response patterns across species to carbon dioxide emission. Such a connection would help to elucidate the microbial basis for the global nutrient cycles that are essential for life on Earth.

*Kyle is scheduled to join the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a program supported by Schmidt Sciences, in the Fall of 2024.*

Related

Insights

* [BlogMay 22, 2024

  ## AI as a Great Teacher for Molecular Dynamic Modeling](https://datascience.uchicago.edu/insights/ai-as-a-great-teacher-for-molecular-dynamic-modeling/)
* [BlogMay 16, 2024

  ## Expanding Our Vocabulary of Vision Using AI](https://datascience.uchicago.edu/insights/expanding-our-vocabulary-of-vision-using-ai/)
* [BlogJun 06, 2024

  ## Behind Automatic Video Semantic Segmentation](https://datascience.uchicago.edu/insights/behind-automatic-video-semantic-segmentation/)
* [BlogJul 29, 2024

  ## Does Political Polarization Really Undermine Democracy? Maybe Not](https://datascience.uchicago.edu/insights/does-political-polarization-really-undermine-democracy-maybe-not/)

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
[![Fig: Formation of HIV capsid simulated by a coarse-grained model.
From: https://www.google.com/url?q=https://www.science.org/doi/epdf/10.1126/sciadv.add7434&sa=D&source=docs&ust=1715014663521469&usg=AOvVaw3fATTBC_yAvxPv6WPYI17_](https://datascience.uchicago.edu/wp-content/uploads/2024/05/HIV-capsid-750x500.png)

[Image: Fig: Formation of HIV capsid simulated by a coarse-grained model.
From: https://www.google.com/url?q=https://www.science.org/doi/epdf/10.1126/sciadv.add7434&sa=D&source=docs&ust=1715014663521469&usg=AOvVaw3fATTBC\_yAvxPv6WPYI17\_]

BlogMay 22, 2024

## AI as a Great Teacher for Molecular Dynamic Modeling](https://datascience.uchicago.edu/insights/ai-as-a-great-teacher-for-molecular-dynamic-modeling/)
[![AI methods and models have enabled a huge leap in our understanding of how images are processed in the brain.
We used to describe visual neurons as “edge detectors” and “face detectors”. Using deep neural networks, we have
discovered that images like these (which really can’t be described with words) are richer models of single neurons in
our visual system. I liken these AI-enabled descriptions of neural function, perhaps ironically, to a whole new kind of
vocabulary that neuroscientists can now use to explain the visual system. (Images from various papers including a,b, c, d, e , f)](https://datascience.uchicago.edu/wp-content/uploads/2024/04/f1-750x500.png)

[Image: AI methods and models have enabled a huge leap in our understanding of how images are processed in the brain.
We used to describe visual neurons as “edge detectors” and “face detectors”. Using deep neural networks, we have
discovered that images like these (which really can’t be described with words) are richer models of single neurons in
our visual system. I liken these AI-enabled descriptions of neural function, perhaps ironically, to a whole new kind of
vocabulary that neuroscientists can now use to explain the visual system. (Images from various papers including a,b, c, d, e , f)]

BlogMay 16, 2024

## Expanding Our Vocabulary of Vision Using AI](https://datascience.uchicago.edu/insights/expanding-our-vocabulary-of-vision-using-ai/)