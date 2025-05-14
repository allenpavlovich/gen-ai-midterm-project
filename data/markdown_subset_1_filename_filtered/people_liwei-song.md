---
title: Liwei Song – DSI
original_url: https://datascience.uchicago.edu/people/liwei-song
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

People

# Liwei Song

Currently: Algorithm Scientist, Huawei; Previously: PhD Candidate, Electrical Engineering, Princeton University

**Talk Title:**Systematic Evaluation of Privacy Risks of Machine Learning Models

**Talk Abstract:**Machine learning models are prone to memorizing sensitive data, making them vulnerable to membership inference attacks in which an adversary aims to guess if an input sample was used to train the model. In this talk, we show that prior work on membership inference attacks may severely underestimate the privacy risks by relying solely on training custom neural network classifiers to perform attacks and focusing only on aggregate results over data samples, such as the attack accuracy.

To overcome these limitations, we first propose to benchmark membership inference privacy risks by improving existing non-neural network based inference attacks and proposing a new inference attack method based on a modification of prediction entropy. Using our benchmark attacks, we demonstrate that existing membership inference defense approaches are not as effective as previously reported.

Next, we introduce a new approach for fine-grained privacy analysis by formulating and deriving a new metric called the privacy risk score. Our privacy risk score metric measures an individual sample’s likelihood of being a training member, which allows an adversary to perform membership inference attacks with high confidence. We experimentally validate the effectiveness of the privacy risk score metric and demonstrate the distribution of privacy risk scores across individual samples is heterogeneous. Our work emphasizes the importance of a systematic and rigorous evaluation of privacy risks of machine learning models.

**Bio:**Liwei Song is a fifth-year PhD student in the Department of Electrical Engineering at Princeton University, advised by Prof. Prateek Mittal. Before coming to Princeton, he received his Bachelor’s degree in Electrical Engineering from Peking University.

His current research focus is on investigating security and privacy issues of machine learning models, including membership inference attacks, evasion attacks, and backdoor attacks. His evaluation methods on membership inference have been integrated into Google’s TensorFlow Privacy library. Besides that, he has also worked on attacking voice assistants with ultrasound, which received widespread media coverage, including BBC News and New York Times.