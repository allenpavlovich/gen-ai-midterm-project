---
title: Yi Wu – DSI
original_url: https://datascience.uchicago.edu/people/yi-wu
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

# Yi Wu

PhD Student, University of Toronto

**Bio**: Denny Wu is a Ph.D. candidate at the University of Toronto and the Vector Institute for Artificial Intelligence, under the supervision of Jimmy Ba and Murat A. Erdogdu. He also maintains close collaboration with the University of Tokyo and RIKEN AIP, where he is currently working with Taiji Suzuki and Atsushi Nitanda. Denny is interested in developing a theoretical understanding (e.g., optimization and generalization) of modern machine learning systems, especially overparameterized models such as neural networks, using tools from high-dimensional statistics.

**Talk Title**: How neural network learns representation: a random matrix theory perspective

**Talk Abstract**: Random matrix theory (RMT) provides powerful tools to characterize the performance of random neural networks in high dimensions. However, it is not clear if similar tools can be applied to trained neural network where the parameters are no longer i.i.d. due to gradient-based learning. In this work we use RMT to precisely quantify the benefit of feature learning in the “early phase” of gradient descent training. We study the first gradient step under the MSE loss on the first-layer weights W in a two-layer neural network. In the proportional asymptotic limit and an idealized student-teacher setting, we show that the gradient update contains a rank-1 “spike”, which results in an alignment between the weights and the linear component of the teacher model f\*. To understand the impact of this alignment, we compute the asymptotic prediction risk of ridge regression on the conjugate kernel after one feature learning step with learning rate \eta. We consider two scalings of \eta. For small \eta, we establish a Gaussian equivalence property for the trained features, and prove that the learned kernel improves upon the initial random features, but cannot defeat the best linear model. Whereas for sufficiently large \eta, we prove that for certain f\*, the same ridge estimator goes beyond this “linear regime” and outperforms a wide range of (fixed) kernels. Our results demonstrate that even one gradient step can lead to considerable advantage over random features, and highlight the role of learning rate scaling in the initial phase of training.