---
title: Developing a smart material that can learn from example – DSI
original_url: https://datascience.uchicago.edu/insights/developing-a-smart-material-that-can-learn-from-example
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogSep 03, 2024

# Developing a smart material that can learn from example

Rituparno Mandal, Data Science Institute Postdoctoral Fellow

A baby bird must learn to fly in order to leave the nest. One way for them to learn is by example – they see their parent’s behavior, and they repeat it. If we had the right teacher, is it possible to get an origami bird to learn how to flap its wings? In other words, how can we teach inanimate objects to reproduce life-like behaviors?

In our recent [study](https://arxiv.org/abs/2406.07856), we addressed some of these questions by expanding the paradigm of [physical learning](https://www.annualreviews.org/doi/abs/10.1146/annurev-conmatphys-040821-113439): an emerging field in science and engineering in which (meta)materials acquire desired behaviors by exposure to examples.

!

**Figure 1a-d. Learning dynamic states.** Figures 1a-b show the general strategy: during a training period (fig. 1a), a time-dependent state is imposed on the system. This is pictured by an origami bird whose wings are periodically moved by an external agent. After training (fig. 1b), a retrieval period during which the physical system evolves under the learned dynamics should lead to a dynamic state that matches the training as best as possible. (fig. 1c and 1d) Demonstration of the training and retrieval procedure using a programmable LEGO toy. The angular positions of two motors are imposed by hand during a training phase (fig. 1c), during which couplings between the motors are learned. Dynamics during retrieval, with learned couplings, can produce fixed points as well as dynamic states where the angles constantly change (fig. 1d). See this [video](https://uchicagoedu-my.sharepoint.com/personal/rituparno_uchicago_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Frituparno%5Fuchicago%5Fedu%2FDocuments%2FAttachments%2Fmov%5Fsummary%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E4ee42a12%2Da4f7%2D4ff7%2D8df9%2Dafd67c400b89&ga=1) for a detailed description.

We know biological systems adapt to their environment by changing their behavior in response to past events as captured by the saying, once bitten, twice shy.  In the brain, for instance, neurons wire together if they fire together. But the ability to learn is not limited to sentient or animate beings; it can emerge in natural physical processes. Inanimate systems can also evolve their microscopic interactions to effectively learn desired behaviors after experiencing examples of that behavior, a phenomenon referred to previously as physical learning. So far, physical learning has been applied to learn static properties, such as to achieving a material with desired mechanical properties or recalling certain self-assembled structures. In our recent article, we ask: how can a physical system learn time-dependent functionalities like pathways, trajectories, or dynamic states?

The essence of our approach is conceptualized schematically in Fig.1: an external agent first imposes a dynamic state that breaks time-reversal symmetry on the system during a period called training (e.g. moves the wings of the origami bird in Fig.1a). (Refer to the [video demonstration](https://uchicagoedu-my.sharepoint.com/personal/rituparno_uchicago_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Frituparno%5Fuchicago%5Fedu%2FDocuments%2FAttachments%2Fmov%5Fsummary%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Efaea3ba6%2D0eb3%2D40e1%2D859b%2Dd3d54169174e&ga=1)). Note we say that a process has time reversal symmetry if a recording of the process looks similar whether it is played forward or in reverse. Next, during a period known as retrieval, the desired time-dependent state (e.g. wings flapping) can be recovered as the system evolves according to interactions learned during the training (Fig.1b).

In our paper, we identify the two ingredients needed to learn time-dependent behaviors that are common across all experimental platforms: (i) learning rules that are dependent on the history of the training process and (ii) exposure to examples that break time-reversal symmetry during training. After providing a hands-on demonstration of these requirements using programmable LEGO toys, we turn to realistic particle-based simulations (refer to the [video demonstration](https://uchicagoedu-my.sharepoint.com/personal/rituparno_uchicago_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Frituparno%5Fuchicago%5Fedu%2FDocuments%2FAttachments%2Fmov%5Fsummary%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Efaea3ba6%2D0eb3%2D40e1%2D859b%2Dd3d54169174e&ga=1)). Instead of programming the training rules by hand, we explain how they emerge from simple physico-chemical processes involving the causal propagation of chemical fields released and sensed by these particles. This rich phenomenology is captured by a modified spin model amenable to analytical treatment.

Our research motivates exploring intelligent, trainable particles that can self-assemble into structures that move or change shape on demand, via the retrieval of the dynamic behavior previously seen during training. This strategy can not only be applied in robotic matter by directly programming a computer, but also in physico-chemical active matter systems where the process of learning naturally emerges. The principles illustrated here provide a step towards [von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann)‘s dream of engineering synthetic systems with life-like behaviors and shed light on how artificial life itself may originate from primitive components capable of adapting to their environment.

Study co-authors:

Rosalind Huang, Undergrad: James Franck Institute & Department of Physics, The University of Chicago

Michel Fruchart, CNRS researcher (CR): Gulliver, ESPCI Paris, Université PSL, CNRS

Pepijn G. Moerman, Assistant Professor: Chemical Engineering and Chemistry, Eindhoven University of Technology

Suriyanarayanan Vaikuntanathan, Professor: James Franck Institute and Department of Chemistry, University of Chicago

Arvind Murugan, Associate Professor: Department of Physics, The University of Chicago

Vincenzo Vitelli, Professor: James Franck Institute, Kadanoff Center for Theoretical Physics & Department of Physics, The University of Chicago

## More on this topic

[!

BlogMar 13, 2025

## Data Ecology Faculty Co-Director Bridget Fahey Writes About Congressional Authority Over Government Data](https://datascience.uchicago.edu/insights/data-ecology-faculty-co-director-bridget-fahey-writes-about-congressional-authority-over-government-data/)
[![Fig 1. Percentage of broadband-serviceable locations (BSLs) with at least one submitted challenge per US state or territory. Nebraska had strong participation in the challenge process, followed by Virginia, New Mexico, and Maine. Most states and territories have low participation rates.](https://datascience.uchicago.edu/wp-content/uploads/2024/08/Fig1-750x500.png)

[Image: Fig 1. Percentage of broadband-serviceable locations (BSLs) with at least one submitted challenge per US state or territory. Nebraska had strong participation in the challenge process, followed by Virginia, New Mexico, and Maine. Most states and territories have low participation rates.]

BlogAug 29, 2024

## The Challenging Path to Internet Broadband Access Equity](https://datascience.uchicago.edu/insights/the-challenging-path-to-internet-broadband-access-equity/)
[!

BlogJul 29, 2024

## Does Political Polarization Really Undermine Democracy? Maybe Not](https://datascience.uchicago.edu/insights/does-political-polarization-really-undermine-democracy-maybe-not/)
[![A video frame example from Cityscape dataset where different colors denote different labels in pixel level. For example, red means person and light blue means sky.](https://datascience.uchicago.edu/wp-content/uploads/2024/05/cityscape-750x500.png)

[Image: A video frame example from Cityscape dataset where different colors denote different labels in pixel level. For example, red means person and light blue means sky.]

BlogJun 06, 2024

## Behind Automatic Video Semantic Segmentation](https://datascience.uchicago.edu/insights/behind-automatic-video-semantic-segmentation/)