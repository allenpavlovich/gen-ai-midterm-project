---
title: Chao Ma – DSI
original_url: https://datascience.uchicago.edu/people/chao-ma
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

# Chao Ma

Szego Assistant Professor, Stanford University

**Bio:** Chao Ma is a Szego Assistant Professor in the Department of Mathematics at Stanford University. His research focuses on building mathematical theories for modern machine learning methods. His recent works provided understandings to the implicit regularization effect of various optimization algorithms for neural networks, by studying the interaction between the algorithms and the network structures. Before joining Stanford, Chao obtained his PhD from the Program of Applied and Computational Mathematics at Princeton University, advised by Prof. Weinan E. His thesis mathematically analyzed the approximation and generalization capacity of neural networks.

**Talk Title:** Implicit bias of optimization algorithms for neural networks and their effects on generalization

**Talk Abstract:** Modern neural networks are usually over-parameterized—the number of parameters exceeds the number of training data. In this case the loss functions tend to have many (or even infinite) global minima, which imposes an additional challenge of minima selection on optimization algorithms besides the convergence. Specifically, when training a neural network, the algorithm not only has to find a global minimum, but also needs to select minima with good generalization among many other bad ones. In this talk, I will share a series of works studying the mechanisms that facilitate global minima selection of optimization algorithms. First, with a linear stability theory, we show that stochastic gradient descent (SGD) favors flat and uniform global minima. Then, we build a theoretical connection of flatness and generalization performance based on a common structure of neural networks. Next, we study the global minima selection dynamics—the process that an optimizer leaves bad minima for good ones—in two settings. For a manifold of minima around which the loss function grows quadratically, we derive effective exploration dynamics on the manifold for SGD and Adam, using a quasistatic approach. For a manifold of minima around which the loss function grows subquadratically, we study the behavior and effective dynamics for GD, which also explains the edge of stability phenomenon.