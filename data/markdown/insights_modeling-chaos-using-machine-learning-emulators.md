---
title: Modeling Chaos using Machine Learning Emulators – DSI
original_url: https://datascience.uchicago.edu/insights/modeling-chaos-using-machine-learning-emulators
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogMar 07, 2024

# Modeling Chaos using Machine Learning Emulators

Peter Y. Lu, Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

Chaos is everywhere, from natural processes—such as fluid flow, weather and climate, and biology—to man-made systems—such as the economy, road traffic, and manufacturing. Understanding and accurately modeling chaotic dynamics is critical for addressing many problems in science and engineering. Machine learning models trained to emulate dynamical systems offer a promising new data-driven approach for developing fast and accurate models of chaotic dynamics. However, these trained models, often called *emulators* or *surrogate models*, sometimes struggle to properly capture chaos leading to unrealistic predictions. In [our recent work](https://openreview.net/pdf?id=8xx0pyMOW1) published at NeurIPS 2023, we propose two new methods for training emulators to accurately model chaotic systems, including an approach inspired by methods in computer vision used for image recognition and generative AI.

Machine learning approaches that use observational or experimental data to emulate dynamical systems have become increasingly popular over the past few years. These emulators aim to capture the dynamics of complex, high-dimensional systems like weather and climate. In principle, emulators will allow us to perform fast and accurate simulations for forecasting, uncertainty quantification, and parameter estimation. However, training emulators to model chaotic systems has proved to be tricky, especially in noisy settings.

!

An emulator for weather forecasting (top) trained on global weather data (bottom). Source: https://github.com/NVlabs/FourCastNet

One key feature of chaotic dynamics is their high sensitivity to initial conditions which is often referred to colloquially as “the butterfly effect”: small changes to an initial state—like a butterfly flapping its wings—can cause large changes in future states—like the location of a tornado. This means that even a tiny amount of noise in the data makes long-term forecasting impossible and precise short-term predictions very difficult. Accurate forecasts of chaotic systems, like the weather, are fundamentally limited by the properties of the chaos. If this is the case, should we simply give up on making long-term predictions?

The answer is both yes and no. Yes, even with machine learning, we will never be able to predict whether it will rain in Chicago more than a few weeks ahead of time (Sorry to all the couples planning outdoor summer weddings!). No, we should not give up completely because, while exact forecasts are impossible, we can still make useful statistical predictions about the future, such as the increasing frequency of hurricanes due to climate change. In fact, these statistical properties—collectively known as the [*chaotic attractor*](https://en.wikipedia.org/wiki/Chaos_theory)—are precisely what scientists focus on when developing models for chaotic systems.

!

Demonstrating the butterfly effect: Two trajectories from the Lorenz-63 system (a standard simple example of chaos) with slightly different initial conditions that quickly diverge (left) but are statistically similar because they both lie on the same chaotic attractor as seen in the 3D scatter plot (right).

Despite these well-known properties of chaotic dynamics, most current approaches for training emulators still focus on short-term forecasting metrics such as the root mean squared error (RMSE). For extremely clean data with high-resolution measurements, the standard training methods are sufficient to learn the correct dynamics since chaotic systems are, after all, deterministic. However, when using noisy or low-resolution data, which is the norm in real-world applications, these training methods often produce emulators that fail to capture the correct long-term statistical behaviors of the system.

!

An emulator trained on the Lorenz-63 system with good short-term predictions (1-Step) but poor long-term behavior (Autonomous).

We address this problem by developing new training methods that encourage the emulator to match long-term statistical properties of the chaotic dynamics—which, again, we refer to as the chaotic attractor. We propose two approaches for achieving this:

1. **Physics-informed Optimal Transport**: Choose a set of relevant summary statistics based on expert knowledge: for example, a climate scientist might pick the global mean temperature or the frequency of hurricanes. Then, during training, use an *optimal transport* metric—a way of quantifying discrepancies between distributions—to match the distribution of the summary statistics produced by the emulator to the distribution seen in the data.
2. **Unsupervised Contrastive Learning**: Automatically choose relevant statistics that characterize the chaotic attractor by using *contrastive learning*, a machine learning approach initially developed for learning useful image representations for image recognition tasks and generative AI. Then, during training, match the learned relevant statistics of the emulator to the statistics of the data.

The distinction between the two methods lies primarily in how we choose the relevant statistics: either we pick (1) based on expert scientific knowledge or (2) automatically using machine learning. In both cases, we train emulators to generate predictions that match the long-term statistics of the data rather than just short-term forecasts. This results in much more robust emulators that, even when trained on noisy data, produce predictions with the same statistical properties as the real underlying chaotic dynamics.

The best we can hope for when modeling chaos is either short-term forecasts or long-term statistical predictions, and emulators trained using the newly proposed methods give us the best of both worlds. Emulators are already being used in a wide range of applications such as weather prediction, climate modeling, fluid dynamics, and biophysics. Our approach and other promising recent developments in emulator design and training are bringing us closer to the goal of having fast, accurate, and perhaps even interpretable data-driven models for complex dynamical systems, which will help us answer many basic scientific questions as well as solve challenging engineering problems.

Paper citation:

Jiang, R., Lu, P. Y., Orlova, E., & Willett, R. (2023). [Training neural operators to preserve invariant measures of chaotic attractors](https://proceedings.neurips.cc/paper_files/paper/2023/hash/57d7e7e1593ad1ab6818c258fa5654ce-Abstract-Conference.html). *Advances in Neural Information Processing Systems*, *36*.

*This work was supported by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Program of Schmidt Futures.*

Related

Research

* [AI + Science

  ## Advancing Molecular Measurement with Machine Learning](https://datascience.uchicago.edu/research/advancing-molecular-measurement-with-machine-learning/)
* [Research Initiative

  ## AI + Science](https://datascience.uchicago.edu/research/ai-science/)

Insights

* [BlogMar 21, 2024

  ## Spatial Immunity: A new perspective enabled by computer vision](https://datascience.uchicago.edu/insights/spatial-immunity-a-new-perspective-enabled-by-computer-vision/)

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