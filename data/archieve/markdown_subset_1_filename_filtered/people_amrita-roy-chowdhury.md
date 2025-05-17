---
title: Amrita Roy Chowdhury – DSI
original_url: https://datascience.uchicago.edu/people/amrita-roy-chowdhury
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

# Amrita Roy Chowdhury

Currently: CRA/CCC Computing Innovation Postdoctoral Fellow, UC San Diego; Previously: PhD Student, University of Wisconsin

**Bio:**Amrita Roy Chowdhury is a PhD student at the University of Wisconsin-Madison and is advised by Prof. Somesh Jha. She completed her Bachelor of Engineering in Computer Science from the Indian Institute of Engineering Science and Technology, Shibpur where she was awarded the President of India Gold Medal. Her work explores the synergy between differential privacy and cryptography through novel algorithms that expose the rich interconnections between the two areas, both in theory and practice. She has been recognized as a Rising Star in EECS at MIT, 2021 and UC Berkeley, 2020, and a 2021 Facebook Fellowship finalist. She has also been awarded the 2021 CRA/CCC Computing Innovation Fellowship.

**Talk Title:**Crypt$\epsilon$: Crypto-Assisted Differential Privacy on Untrusted Servers

**Talk Abstract:**Differential privacy (DP) is currently the de-facto standard for achieving privacy in data analysis, which is typically implemented either in the ”central” or ”local” model. The local model has been more popular for commercial deployments as it does not require a trusted data collector. This increased privacy, however, comes at the cost of utility and algorithmic expressibility as compared to the central model.

In this talk, I will be presenting Crypt$\epsilon$, a system and programming framework that (1) achieves the accuracy guarantees and algorithmic expressibility of the central model (2) without any trusted data collector like in the local model. Crypt$\epsilon$ achieves the ”best of both worlds” by employing two non-colluding untrusted servers that run DP programs on encrypted data from the data owners. In theory, straightforward implementations of DP programs using off-the-shelf secure multi-party computation tools can achieve the above goal. However, in practice, they are beset with many challenges like poor performance and tricky security proofs. To this end, Crypt$\epsilon$ allows data analysts to author logical DP programs that are automatically translated to secure protocols that work on encrypted data. These protocols ensure that the untrusted servers learn nothing more than the noisy outputs, thereby guaranteeing DP for all Crypt$\epsilon$ programs. Crypt$\epsilon$ supports a rich class of DP programs that can be expressed via a small set of transformation and measurement operators followed by arbitrary post-processing. Further, I will talk about a novel performance optimization that leverages the fact that the output is noisy. Consequently, Crypt$\epsilon$ achieves performance that is practical for real-world usage.