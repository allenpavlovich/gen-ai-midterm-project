---
title: Leveraging machine learning to uncover the lives and deaths of massive stars using gravitational waves – DSI
original_url: https://datascience.uchicago.edu/insights/leveraging-machine-learning-to-uncover-the-lives-and-deaths-of-massive-stars-using-gravitational-waves
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogMar 28, 2024

# Leveraging machine learning to uncover the lives and deaths of massive stars using gravitational waves

Colm Talbot, Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

Observations of merging binary black hole systems allow us to probe the behavior of matter under extreme temperatures and pressures, the cosmic expansion rate of the Universe, and the fundamental nature of gravity. The precision with which we can extract this information is limited by the number of observed sources; the more systems we observe, the more we can learn about astrophysics and cosmology. However, as the precision of our measurements increases it becomes increasingly important to interrogate sources of bias intrinsic to our analysis methods. Given the number of sources we expect to observe in the coming years, we will need radically new analysis methods to avoid becoming dominated by sources of systematic bias. By combining physical knowledge of the observed systems and AI methods, we can overcome these challenges and face the oncoming tide of observations.

#### **A New Window on the Universe**

In September 2015, [a new field of astronomy was born](https://www.ligo.org/detections/GW150914.php) with the observation of gravitational waves from the collision of two black holes over a billion light years away by the twin [LIGO](https://www.ligo.caltech.edu/) detectors. In the intervening years, the LIGO detectors have been joined by the [Virgo](https://www.virgo-gw.eu/) detector and similar signals have been observed from over 100 additional merging binaries. Despite this large and growing number of observations, many more signals are not resolvable by current detectors due to observational selection bias. An example of this selection bias is that more massive binaries radiate more than less massive binaries and so are observable at greater distances. Over the next decade, upgrades to existing instruments will increase our sensitivity and increase the observed catalog to many hundreds by the end of the decade. In addition, the planned [next](https://cosmicexplorer.org/) [generation](https://www.et-gw.eu/) of detectors is expected to observe every binary black hole merger in the Universe, accumulating a new binary every few minutes.

!

This is a standard figure used in the field of astrophysics, created by Aaron Geller of Northwestern University.

Each of these mergers is the end of an evolutionary path from pairs of stars initially more tens of times massive than the Sun. Over their lives, these stars passed through a [complex series of evolutionary phases](https://www.sciencedirect.com/science/article/pii/S0370157322000175) and interactions with their companion star. This path includes extended periods of steady mass loss during the lifetime of the star, dramatic mass loss during a supernova explosion, and mass transfer between the two stars. Each of these effects is determined by currently unknown physics. Understanding the physical processes governing this evolutionary path is a key goal of gravitational-wave astronomy.

#### **From Data to Astrophysics**

Extracting this information requires performing a simultaneous analysis of all of the observed signals while accounting for the observation bias. Individual events are characterized by assuming that the instrumental noise around the time of the merger is well understood. The observation bias is characterized by adding simulated signals to the observed data and counting what fraction of these signals are recovered. In practice, the population analysis is performed using a multi-stage framework where the individual observations and the observation bias are analyzed with an initial simple model and then combined using physically-motivated models.

Using this approach we have learned that:

* black holes between twenty and a hundred times the mass of the Sun exist and merge; a previously unobserved population.
* there is an excess of black holes approximately 35 times the mass of the Sun implying there is a characteristic mass scale to the processes of stellar evolution.
* most merging black holes rotate slowly, in contrast to black holes observed in the Milky Way.

#### **Growing Pains**

Previous research has shown that AI methods can solve gravitational-wave data analysis problems, in some cases far more efficiently than classical methods. However, these methods also struggle to deal with the large volume of data that will be available in the coming years. As a Schmidt fellow, I am working to combine theoretical knowledge about the signals we observe with simulation-based inference methods to overcome this limitation and allow us to leverage the growing catalog of binary black hole mergers fully.

For example, while the statistical uncertainty in our inference decreases as the catalog grows, the systematic error intrinsic to our analysis method [grows approximately quadratically](https://academic.oup.com/mnras/article/526/3/3495/7285822) with the size of the observed population. This systematic error is driven by the method used to account for the observational bias. In [previous work](https://ui.adsabs.harvard.edu/link_gateway/2022ApJ...927...76T/doi:10.3847/1538-4357/ac4bc0), I demonstrated that by reformulating our analysis as a [density estimation](https://en.wikipedia.org/wiki/Density_estimation) problem we can reduce this systematic error, however, this is simply a band-aid and not a full solution.

I am currently working on using [approximate Bayesian computation](https://en.wikipedia.org/wiki/Approximate_Bayesian_computation) to analyze large sets of observations in a way that is less susceptible to systematic error. An open question in how to perform such analyses is how to efficiently represent the large volume of observed data. I am exploring how we can use theoretically motivated pre-processing stages to avoid the need for large embedding networks that are traditionally used. By combining this theoretical understanding of the problem with AI methods I hope to extract astrophysical insights from gravitational-wave observations with both more robustness and reduced computational cost.

*This work was supported by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Program of Schmidt Futures.*

Related

Research

* [Research Initiative

  ## AI + Science](https://datascience.uchicago.edu/research/ai-science/)

Insights

* [BlogApr 04, 2024

  ## An Intro to Gravitational-Wave Astronomy](https://datascience.uchicago.edu/insights/an-intro-to-gravitational-wave-astronomy/)
* [BlogMay 09, 2024

  ## Teaching materials to adapt](https://datascience.uchicago.edu/insights/teaching-materials-to-adapt/)
* [BlogApr 11, 2024

  ## Finding the likely causes when potential explanatory factors look alike](https://datascience.uchicago.edu/insights/finding-the-likely-causes-when-potential-explanatory-factors-look-alike/)

News

* [DSI NewsMay 22, 2024

  ## Eric and Wendy Schmidt AI in Science Postdoctoral Fellows host first-ever hackathon](https://datascience.uchicago.edu/news/eric-and-wendy-schmidt-ai-in-science-postdoctoral-fellows-host-first-ever-hackathon/)

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