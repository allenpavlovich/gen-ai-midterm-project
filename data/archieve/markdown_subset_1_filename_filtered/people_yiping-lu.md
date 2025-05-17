---
title: Yiping Lu – DSI
original_url: https://datascience.uchicago.edu/people/yiping-lu
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

# Yiping Lu

PhD Student, Stanford University

**Bio**: Yiping Lu is a fourth-year Ph.D. student at ICME Stanford, working with Lexing Ying and Jose Blanchet. Before that, he got his Bachelor’s degree in computational mathematics and information science at Peking University. His research interest lies in Non-parametric Statistics, Inverse Problems, Stochastic Modeling, and Econometrics. His research aims to design algorithms that combine data-driven techniques with (differential equation/structural) modeling and provide corresponding statistical and computational guarantees. Yiping’s research is supported by the Stanford Interdisciplinary Graduate Fellowship.

**Talk Title**: Machine Learning for Differential equations: Statistics, Optimization and MultiLevel Learning

**Talk Abstract**: In this talk, we aim to study the statistical limits and optimal algorithms to solve Elliptic PDEs from random samples. In the first part of my talk, I’ll study the statistical and optimization property of learning the Elliptic inverse problem using the Deep Ritz Method (DRM) and Physics Informed Neural Networks (PINNs). We provided a minimax lower bound for this problem and discovered that the variance in DRM leads sample complexity being suboptimal. Based on this observation, we proposed a modification of DRM with optimal sample complexity. Then I’ll introduce the optimization property of a class of Sobolev norms as the objective function. Although early stopped gradient descent for all the objective functions is statistically optimal, I observed that using the Sobolev norm can accelerate training. Combining the information from the two papers, we can conclude that DRM is fast for the high dimensional smoothing function due to the low computational cost of each iteration. But for low dimensional rough functions, we should use PINN. In the second part of my talk, I’ll talk about the statistical limit of learning linear operator learning, where both the input and output space are infinite-dimensional. We showed that proper bias and variance trade-offs could lead to optimal learning rates. The optimal learning rate is different from learning finite-dimensional linear operators. We also illustrate how this theory can inspire a multilevel machine learning algorithm. Our theory has wide application in learning differential operators and generative modeling.