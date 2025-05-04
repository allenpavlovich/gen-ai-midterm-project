---
title: What’s Game-Theoretic About Statistics? A Game-Theoretic Notion of Evidence and Cooperative Skepticism – DSI
original_url: https://datascience.uchicago.edu/insights/whats-game-theoretic-about-statistics-a-game-theoretic-notion-of-evidence-and-cooperative-skepticism
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogOct 31, 2024

# What’s Game-Theoretic About Statistics? A Game-Theoretic Notion of Evidence and Cooperative Skepticism

Yo Joong “YJ” Choe, Data Science Institute Postdoctoral Fellow

Much of scientific discovery—be it the existence of a new particle or the effectiveness of a new cancer treatment—directly relies on a quantified notion of *evidence* obtained from data. Yet, the most widespread notion of evidence, known as the **p-value**, has a number of issues. The p-value is easy to misuse and hard to understand; further, combining different p-values is generally difficult.

So, is there an alternative that can avoid these issues? It turns out that there is a promising alternative based on *game-theoretic* ideas, called the **[e-value](https://en.wikipedia.org/wiki/E-values)**. After reviewing this game-theoretic notion of evidence, I will introduce [my recent work](https://arxiv.org/abs/2402.09698), joint with Aaditya Ramdas (Carnegie Mellon University), where we develop a general approach to combining game-theoretic evidence in the challenging case of asymmetric information.

### E-Value: A Game-Theoretic Notion of Evidence

Given a *null hypothesis* (for example, that a drug has no effect on a health outcome), how do we quantify the evidence against it based on observed data? In classical hypothesis testing, we typically compute a p-value, which is a number between 0 and 1 that is unlikely to be small (say, less than 0.05) if the null hypothesis is true. If we observe a small p-value, we take it as evidence that the null hypothesis is unlikely to be true. While mathematically sound, this complicated and indirect definition of a p-value is arguably *the* culprit for many instances of [“p-hacking”](https://royalsocietypublishing.org/doi/10.1098/rsos.220346) in scientific research.

In search of a more intuitive and robust notion of evidence, some statisticians have revisited a [centuries-old](https://www.probabilityandfinance.com/articles/32.pdf) idea underlying probability theory and statistics: the idea of understanding probabilities through *betting games*. In the resulting framework known as **[testing-by-betting](https://doi.org/10.1111/rssa.12647)**, we cast a hypothesis testing problem as a perfect-information game, in which the null hypothesis corresponds to a probability (or a family of probabilities) proposed by a bookmaker. For example, a null hypothesis saying “this coin is fair” can be viewed as a bookmaker proposing equal odds on either side of the coin.

Next, a *skeptic* can play this game by betting their money on it. For example, the skeptic may have doubts that the coin is biased towards heads, so they may choose to bet repeatedly a fraction of their budget on heads. Over repeated rounds of the game, the skeptic’s wealth (relative to their initial wealth) *directly* captures the evidence against the null hypothesis: the more wealth they accumulate, the more evidence the skeptic has against the coin being fair (see Figures 1 & 2). The skeptic’s accumulated wealth in this game is called an *e-value*, short for “evidence value”, or simply a *betting score*.

!

*Figure 1: In a roulette table, a gambler who believes that the odds are higher for the ball to land on red may choose to repeatedly bet on red, and make money if they are right. Analogously in testing-by-betting, a skeptic who is doubtful of the proposed null hypothesis may repeatedly bet against it, and their resulting wealth quantifies evidence against the null. The larger the wealth, the less likely it is that the null is true. (Photo:* [*Wikipedia*](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/13-02-27-spielbank-wiesbaden-by-RalfR-094.jpg/2560px-13-02-27-spielbank-wiesbaden-by-RalfR-094.jpg)*)*

!

*Figure 2: As more data is observed, an e-value remains small (less than one) when the data is generated from a null distribution; it can grow large when the data is instead simulated from an alternative. Here, e-values are computed using the* [*aGRAPA method*](https://doi.org/10.1093/jrsssb/qkad009)*.*

In recent years, a growing number of statisticians have advocated for the use of e-values over p-values. Unlike p-values, e-values have the “what-you-see-is-what-you-get” property: if I observed an e-value of 100 using the data, then effectively I was able to multiply my wealth *100 (!) times* by betting against the odds put forth by the null hypothesis. This is quite an unlikely outcome unless the null hypothesis was wrong. In the betting view, it is also easier to intuitively capture the size of an e-value; in contrast, it is not obvious how to compare p-values of, say, 0.002 and 0.01, not to mention the fuzzy meaning of a large p-value of, say, 0.37. E-values thus help alleviate dichotomous thinking, which contributes to the [“replication crisis” in science](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9405484).

Aside from their intuitive appeal, e-values offer (at least) two tangible benefits. First, e-values allow for **[anytime-valid inference](https://doi.org/10.1214/23-STS894)** in sequential experiments: even when we choose to stop the experiment *after* observing some data points, the resulting e-value is a statistically valid measure of evidence at that *data-dependent* sample size. This allows the experimenter to avoid a major cause of p-hacking, namely when researchers “fish” for a small enough p-value by collecting more data until they find one (known as *optional stopping*; you will surely run into a false positive this way). Second, generally speaking, e-values can be combined seamlessly via averaging, even when they are arbitrarily dependent; our recent work closely examines this characteristic of e-values.

### Cooperative Skepticism: A General Framework for Combining Evidence Under Information Asymmetry

Advancing this exciting frontier of statistics, our recent work ([Choe & Ramdas, 2024](https://arxiv.org/abs/2402.09698)) develops a general approach to combining e-values when the evidence is obtained sequentially from *asymmetric information sources*.

Recent work has shown that we can design e-values for complex families of null hypotheses, e.g., for sequentially testing whether the data is [random](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) and whether the input and output of the data are [statistically independent](https://en.wikipedia.org/wiki/Independence_(probability_theory)). These can be important diagnostic tests when building machine learning models that rely on such assumptions (or the lack thereof). For these complex hypotheses, a [popular](https://dl.acm.org/doi/10.5555/3666122.3668441) [strategy](https://doi.org/10.1093/biomet/asae023) for designing powerful e-values is to *limit* the information available to the skeptic.

However, when using this strategy, the “anytime-validity” of the resulting e-value can be quite subtle. In particular, this limited-information e-value is not valid at data-dependent sample sizes, and thus it cannot be readily combined with other e-values (that are anytime-valid). More generally, if two skeptics play the game with asymmetric information sets, then their resulting wealth cannot be combined as seamlessly as usual.

To address this challenge, we make two main contributions in our recent work:

1. We propose a general approach to combining e-values obtained across different information sets using **adjusters**, which are functions that transform an e-value that is only valid under a restricted set of information to one that is valid under full information (the data). In particular, using an adjuster ensures that the combined e-value is valid at data-dependent sample sizes (see Figure 3).
2. We show how using adjusters can be *necessary* for ensuring the validity of the combined e-value, in the case of asymmetric information. The approach is applicable to *any* e-values for complex hypotheses in sequential experiments.

!

*Figure 3: For complex hypotheses like “data is random”, an unadjusted e-value may lack validity at data-dependent sample sizes (yellow; many e-values exceed 1), preventing it from being combined with other e-values via averaging. Applying an adjuster resolves this issue (green). The plot shows e-values computed over 100 repeated simulations of random data; dots indicate the final (data-dependent) sample size in each run.*

We broadly refer to the overall process of combining e-values as **cooperative skepticism**, as it involves pooling evidence from multiple skeptics who each play the game having different information sets. As adjusters incur a relatively small loss of evidence and a negligible computational cost, they can be used in any (sequential) hypothesis testing scenario where the e-value is only valid under limited information. 

*This post is based on joint work with Aaditya Ramdas (Carnegie Mellon University).*