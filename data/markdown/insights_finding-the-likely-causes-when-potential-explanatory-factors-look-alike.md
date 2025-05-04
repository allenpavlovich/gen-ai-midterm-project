---
title: Finding the likely causes when potential explanatory factors look alike – DSI
original_url: https://datascience.uchicago.edu/insights/finding-the-likely-causes-when-potential-explanatory-factors-look-alike
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogApr 11, 2024

# Finding the likely causes when potential explanatory factors look alike

William Denault, Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

Suppose you are a scientist interested in investigating if there is a link between exposure to car pollutants during pregnancy and the amount of brain white matter at birth. A starting hypothesis you would like to test could be: is an *increase* of a specific pollutant associated with a reduction (or increase) of white matter in newborns? A typical study to test this hypothesis would involve recruiting pregnant women, measuring the average amount of pollutants they are exposed to throughout their pregnancy, and measuring the newborn’s proportion of white matter, which is a measure of connectivity. After the collection, the data analysis would involve assessing if at least one of the car pollutants is correlated with the newborn’s brain measurements. It is now well established that exposure to car pollutants during pregnancy is associated with reduced white matter proportion in newborns. A natural follow-up question *would be among all these car pollutants* which is likely to cause a reduction in white matter? That is when things become more tricky.

Because cars tend to produce the same amount of each pollutant (or at least the proportion of pollutants they emit is somewhat constant), we observe little variation in car pollutant proportion over time in a given city. It would be even worse if we only studied women from the same neighborhood and recruited them during a similar period of time (as we expect the car pollutants to be quite homogeneous within a small area). The main difficulty in trying to corner a potential cause among correlated potential causes is that if pollutant A ( e.g., Carbon Monoxide CO) affects the newborn white matter but pollutant B (e.g., Carbon Dioxide C2O) is often producing along with pollutant A, it is likely that both pollutants will be correlated with newborn white matter proportion.

Correlation has been a primary subject of interest since the early days of statistics. While correlation is often a quantity of [inferential interest](https://en.wikipedia.org/wiki/Statistical_inference) (e.g., predicting house price given its surface), in some cases, it can plague an analysis as it is hard to distinguish between potential causes that are correlated (as described above).

Assume now that exactly two pollutants among four that are affecting newborn white matter. Pollutants 1 and 3, say — and that these two pollutants are each completely correlated with another non-effect pollutant, say pollutants 1 and 2 are perfectly correlated and pollutants 2 and 4. Here, because the pollutants are completely correlated with a non-effect pollutant, it is impossible to confidently select the correct pollutants that are causing health problems. However, it should be possible to conclude that there are (at least) two pollutants that affect white matter,  for the first pollutant that affects white matter it is whether (pollutant 1 or pollutant 2), for the first pollutant that affects white matter it is whether  (pollutant 3 or pollutant 4).

This kind of statement  (pollutant 3 or pollutant 4) is called credible sets in the statistical genetic literature. Credible sets are generally defined as follows. A credible set is a subset of the variables that have at least 95% to contain at least one causal variable. In our example, the pollutants are the variables. Inferring credible sets is referred to as fine mapping.

Until recently, most of the statistical approaches were working well for computing credible sets in the case that exactly one pollutant affects newborn white matter. Recent efforts led by the Stephens’ lab and other groups suggest enhancing previous models by simply iterating them through the data multiple times. For example, suppose I have made an initial guess for the credible sets for the first effect pollutant. Now, I can remove the effect of the pollutant from my data and guess the credible sets for the second effect. Once this is done, we can refine our guess for the first pollutant by removing the effect of the second credible set from the data and continuing to repeat this procedure until convergence.

The example we presented above is quite simple as a maximum of a hundred pollutants and derivatives are being studied, and they can be potentially tested one by one in a lab using mice. The problem becomes much harder in genetics, where scientists try to understand the role of hundreds of thousands of variants on molecular regulation. And in fact, genetic variants tend to be much more correlated than car pollutants. And this complexity increases as we try to understand more complex traits. For example, instead of just trying to see if exposure to car pollutants affects the white matter at birth, we could see if that affects the proportion of white matter throughout childhood.

!

Illustration of our new fin-mapping method (fSuSiE) for fine-mapping dynamic/temporally structured traits. In this example, we consider a pollutant that decreases the amount of white matter during a certain duration during childhood. This effect is displayed in the left column. We are trying to corner the causal pollutant among 100 candidates. The index of the causal pollutant is displayed in red on the right column, and the index of the other candidate pollutants is displayed in black. One approach might be to fine-map each time point independently, for example, using previous fine-mapping methods like SuSiE. In this example, we run SuSiE at each time point to identify the causal pollutant. SuSiE detected the effect of pollutants at only 4 time points (first top four panels). The different 95% credible sets (blue circles) are displayed on the right-hand side. We observe that the PIPs (probabilities of being the causal SNP) are different at each time point. On the other hand, fSuSiE identifies the causal pollutant in a credible set containing a single pollutant (lowest panel). Additionally, fSuSiE estimates the effect of the causal pollutant. The black line is the true effect; the solid blue line is the posterior mean estimate; and the dashed blue lines give the 95% posterior credible bands.

Our current work is generalizing the iterative procedure described here to a more complex model. One of the main difficulties is to find a good trade-off between model complexity and computational efficiency.  More complex models capture more subtle variation in the data but are more costly to estimate. We use ideas from signal processing methods ([wavelet](https://en.wikipedia.org/wiki/Wavelet)) to perform fast iterative procedures to corner genetic variants (or car pollutants) that affect dynamic or spatially structured traits (e.g., white matter development throughout childhood or DNA methylation). We present some of the advantages of our new work in Figure 1.

Coming back to our earlier example where pollutants 1 and 3 affect white matter. The main problem with fine-mapping pollutants that affect temporally-structured traits is that standard fine-mapping may suggest that pollutant 1 affects white matter proportion at birth but then may suggest that pollutant 2 affects white matter at three months. Thus leading to inconsistent results throughout childhood. Using a more advanced model that can look at each child’s trajectory (instead of at each time point separately as normally done) allows for more consistent and interpretable results. We illustrate this advantage in Figure 1.

*This work was supported by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Program of Schmidt Futures.*

Related

Research

* [Research Initiative

  ## AI + Science](https://datascience.uchicago.edu/research/ai-science/)

Insights

* [BlogApr 04, 2024

  ## An Intro to Gravitational-Wave Astronomy](https://datascience.uchicago.edu/insights/an-intro-to-gravitational-wave-astronomy/)
* [BlogMar 28, 2024

  ## Leveraging machine learning to uncover the lives and deaths of massive stars using gravitational waves](https://datascience.uchicago.edu/insights/leveraging-machine-learning-to-uncover-the-lives-and-deaths-of-massive-stars-using-gravitational-waves/)
* [BlogApr 18, 2024

  ## Uncovering Patterns in Structure for Voltage Sensing Membrane Proteins with Machine Learning](https://datascience.uchicago.edu/insights/uncovering-patterns-in-structure-for-voltage-sensing-membrane-proteins-with-machine-learning/)
* [BlogApr 25, 2024

  ## Towards New Physics at Future Colliders: Machine Learning Optimized Detector and Accelerator Design](https://datascience.uchicago.edu/insights/towards-new-physics-at-future-colliders-machine-learning-optimized-detector-and-accelerator-design/)

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