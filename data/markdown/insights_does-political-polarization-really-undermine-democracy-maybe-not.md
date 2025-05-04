---
title: Does Political Polarization Really Undermine Democracy? Maybe Not – DSI
original_url: https://datascience.uchicago.edu/insights/does-political-polarization-really-undermine-democracy-maybe-not
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogJul 29, 2024

# Does Political Polarization Really Undermine Democracy? Maybe Not

Isaac Mehlhaff, Data Science Institute Postdoctoral Fellow

We’ve all heard the warnings: [our political systems are becoming increasingly polarized](https://www.pewresearch.org/politics/2014/06/12/political-polarization-in-the-american-public/), and this [division threatens the very foundations of democracy](https://www.brookings.edu/articles/reducing-extreme-polarization-is-key-to-stabilizing-democracy/). The logic seems intuitive—as people become more extreme in their views, it becomes harder to find common ground, making compromise and effective governance impossible. But is this widely held belief actually true? [My recent research](https://imehlhaff.net/assets/pdf/democracy.pdf) challenges this assumption, finding little evidence that mass polarization leads to democratic decline. Instead, I show that democratic crises may be driving polarization. 

The key issue is that we didn’t have the data necessary to test whether polarization causes harm to democracies—until now. [Many scholars have used public opinion data](https://www.tandfonline.com/doi/abs/10.1080/13510347.2021.2008912), usually across several countries at a handful of time points, to show that polarization and democratic backsliding often occur together. This observation allows us to say that polarization and backsliding are *correlated*, but knowing that polarization and backsliding often show up in the same place at the same time doesn’t reveal whether this relationship is *causal*.

A common approach to establish causation in quantitative social science research is to conduct an experiment, but randomly manipulating the level of polarization in a country would be unethical, especially if we think it might lead to democratic collapse. When experiments aren’t feasible, another option is to track the same observations over time. That is the approach I took.

I collected over 3.5 million interviews from 35 survey programs, focusing on *ideological polarization*—which captures how far apart people are in their political beliefs—and *affective polarization*, which measures the negativity people feel toward members of other political parties. 

These data have several problems, however. The wordings of survey questions and response options vary, items have different numbers of response categories, and survey programs use different sampling procedures. I didn’t want those sources of variation to show up in polarization estimates, so I designed a complex measurement model that corrects for them and estimates polarization in every country-year, even ones that didn’t have any raw data.

The result was a dataset with polarization estimates in 92 countries from 1971-2019 that [scholars can use to answer important questions](https://imehlhaff.net/PolarCAP/) about mass polarization. To give a sense of the breadth of this dataset, the map below shows how ideological polarization varied around the world in 2010. Darker shaded countries, like the United States, had higher estimated levels of polarization while lighter shaded countries, like Finland, were less polarized.

![A world map showing levels of political polarization in different countries. The U.S. and Australia have high levels of political polarization.](http://datascience.uchicago.edu/wp-content/uploads/2024/07/figure-scaled.jpg)

[Image: A world map showing levels of political polarization in different countries. The U.S. and Australia have high levels of political polarization.]

Using these polarization estimates and similar time series data from the [Varieties of Democracy Project](https://www.v-dem.net/), I replicated the commonly cited correlation between polarization and democracy. But how can we be sure changes in polarization are causing changes in democracy, and not the other way around? To address this, I used statistical techniques developed for time series data that allowed me to isolate the causal effect of polarization on democracy, controlling for other factors that could also be influential.

Results showed that increases in polarization had a negligible effect on democracy. Any slight impact of ideological polarization took over a decade to become meaningful, and affective polarization had virtually no effect even in the long run.

Why do many scholars find a correlation between polarization and democracy, while my causal evidence is muted? When I reversed the relationship and examined the impact of democratic backsliding on polarization, a compelling explanation emerged. Declines in democratic practices consistently predicted subsequent increases in polarization, suggesting the erosion of democratic institutions, such as free and fair elections or protection of civil liberties, might foment mass polarization.

Imagine a society where democratic norms are eroding, and leaders disregard the rule of law. In this climate of fear, people may cling more tightly to their political identities, viewing the “other side” with increasing suspicion and hostility. This sense of threat could drive individuals to adopt more extreme positions, further fueling polarization. While it’s tempting to view polarization as a culprit in democratic backsliding, this research suggests it might be more of a symptom than a cause. 

This is not to say polarization is irrelevant. Even if it doesn’t directly affect democracy, it can exacerbate existing tensions and [make it even more challenging to address the root causes of backsliding](https://journals.sagepub.com/doi/full/10.1177/00027162241228952). However, my research suggests that focusing solely on reducing polarization may be misguided. Instead, we should prioritize strengthening democratic institutions, holding political leaders accountable, and promoting civic engagement.

By addressing the underlying factors that contribute to both democratic backsliding and polarization, we can create a more resilient and inclusive society—one where disagreement is not a threat but an opportunity for constructive debate and progress.

*Isaac’s research is part of the Data Science Institute’s [Data and Democracy Research Initiative](https://datascience.uchicago.edu/research/data-democracy/).*

## People

<!-- Table-like structure detected -->

! 

# Isaac Mehlhaff

Assistant Professor, Department of Political Science, Texas A&M University

Related

Insights

* [BlogJun 06, 2024

  ## Behind Automatic Video Semantic Segmentation](https://datascience.uchicago.edu/insights/behind-automatic-video-semantic-segmentation/)
* [BlogMay 30, 2024

  ## Searching for simplicity in microbial communities](https://datascience.uchicago.edu/insights/searching-for-simplicity-in-microbial-communities/)

## More on this topic

[!

BlogMar 13, 2025

## Data Ecology Faculty Co-Director Bridget Fahey Writes About Congressional Authority Over Government Data](https://datascience.uchicago.edu/insights/data-ecology-faculty-co-director-bridget-fahey-writes-about-congressional-authority-over-government-data/)
[!

BlogFeb 26, 2025

## Federal budget cuts threaten to decimate America’s AI superiority—and other countries are watching](https://datascience.uchicago.edu/insights/federal-budget-cuts-threaten-to-decimate-americas-ai-superiority-and-other-countries-are-watching/)
[![Figures 1a-b show the general strategy: during a training period (fig. 1a), a time-dependent state is imposed on the system. This is pictured by an origami bird whose wings are periodically moved by an external agent. After training (fig. 1b), a retrieval period during which the physical system evolves under the learned dynamics should lead to a dynamic state that matches the training as best as possible. (fig. 1c and 1d) Demonstration of the training and retrieval procedure using a programmable LEGO toy. The angular positions of two motors are imposed by hand during a training phase (fig. 1c), during which couplings between the motors are learned. Dynamics during retrieval, with learned couplings, can produce fixed points as well as dynamic states where the angles constantly change (fig. 1d). See this video for a detailed description.](https://datascience.uchicago.edu/wp-content/uploads/2024/09/x1-750x500.jpeg)

[Image: Figures 1a-b show the general strategy: during a training period (fig. 1a), a time-dependent state is imposed on the system. This is pictured by an origami bird whose wings are periodically moved by an external agent. After training (fig. 1b), a retrieval period during which the physical system evolves under the learned dynamics should lead to a dynamic state that matches the training as best as possible. (fig. 1c and 1d) Demonstration of the training and retrieval procedure using a programmable LEGO toy. The angular positions of two motors are imposed by hand during a training phase (fig. 1c), during which couplings between the motors are learned. Dynamics during retrieval, with learned couplings, can produce fixed points as well as dynamic states where the angles constantly change (fig. 1d). See this video for a detailed description.]

BlogSep 03, 2024

## Developing a smart material that can learn from example](https://datascience.uchicago.edu/insights/developing-a-smart-material-that-can-learn-from-example/)
[![Fig 1. Percentage of broadband-serviceable locations (BSLs) with at least one submitted challenge per US state or territory. Nebraska had strong participation in the challenge process, followed by Virginia, New Mexico, and Maine. Most states and territories have low participation rates.](https://datascience.uchicago.edu/wp-content/uploads/2024/08/Fig1-750x500.png)

[Image: Fig 1. Percentage of broadband-serviceable locations (BSLs) with at least one submitted challenge per US state or territory. Nebraska had strong participation in the challenge process, followed by Virginia, New Mexico, and Maine. Most states and territories have low participation rates.]

BlogAug 29, 2024

## The Challenging Path to Internet Broadband Access Equity](https://datascience.uchicago.edu/insights/the-challenging-path-to-internet-broadband-access-equity/)