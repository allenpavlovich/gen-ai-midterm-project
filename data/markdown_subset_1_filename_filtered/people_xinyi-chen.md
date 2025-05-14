---
title: Xinyi Chen – DSI
original_url: https://datascience.uchicago.edu/people/xinyi-chen
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

# Xinyi Chen

PhD Candidate, Princeton University

**Bio:**Xinyi Chen is a PhD candidate in the Department of Computer Science at Princeton University advised by Prof. Elad Hazan. Her research is at the intersection of machine learning, optimization, and dynamical systems, with a focus on developing provably robust and efficient methods for sequential decision-making and control. Previously, she obtained her undergraduate degree from Princeton in mathematics, where she received the Middleton Miller Prize. She is a recipient of the Siebel Scholarship and the NSF Graduate Research Fellowship, as well as a participant of EECS Rising Stars at UC Berkeley.

**Talk Title:**A Nonstochastic Control Approach to Optimization

**Abstract:** In the modern deep learning pipeline, selecting the best optimization algorithm and the associated set of hyperparameters for a particular problem instance is crucial. The choice of the optimizer can significantly influence the performance of the trained model. However, this is a nonconvex task, and a result, iterative optimization methods such as hypergradient descent lack global optimality guarantees in general.

We propose an online nonstochastic control methodology for mathematical optimization. First, we formalize the setting of meta-optimization, an online learning formulation of learning the best optimization algorithm from a class of methods. The meta-optimization problem over gradient-based methods can be framed as a feedback control problem over the choice of hyperparameters, including the learning rate, momentum, and the preconditioner.

Although the original optimal control problem is nonconvex, we show how recent methods from online nonstochastic control using convex relaxations can be used to overcome the challenge of nonconvexity, and obtain regret guarantees against the best offline solution. This guarantees that in meta-optimization, given a sequence of optimization problems, we can learn a method that attains convergence comparable to that of the best optimization method in hindsight from a class of methods. Finally, we demonstrate empirically that our meta-optimization algorithm can continuously improve given problem instances, and become competitive with the best tuned method among a class of methods.

Contact Info

Website

<https://xinyi.github.io/>