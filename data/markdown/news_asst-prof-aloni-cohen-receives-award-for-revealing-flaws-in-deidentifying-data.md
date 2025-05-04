---
title: Asst. Prof. Aloni Cohen Receives Award For Revealing Flaws in Deidentifying Data – DSI
original_url: https://datascience.uchicago.edu/news/asst-prof-aloni-cohen-receives-award-for-revealing-flaws-in-deidentifying-data
category: news
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

DSI NewsSep 12, 2022

# Asst. Prof. Aloni Cohen Receives Award For Revealing Flaws in Deidentifying Data

In the tug of war between data science and privacy, deidentification is meant to be a compromise. When datasets containing personal information are shared for research or used by companies, they try to disguise data – removing the final one or two digits of a zip code, for example – while still preserving its utility for insight. But while deidentification is often intended to satisfy legal requirements for data privacy, the most commonly used methods stand on shaky technical ground.

!In [a new paper](https://www.usenix.org/conference/usenixsecurity22/presentation/cohen) that received a Distinguished Paper Award at the [USENIX Security Symposium](https://www.usenix.org/conference/usenixsecurity22) in August 2022, DSI Assistant Professor [Aloni Cohen](/people/aloni-cohen/) deals the latest decisive blow against the most popular deidentification techniques. By describing a new kind of attack called “downcoding,” and demonstrating the vulnerability of a deidentified data set from an online education platform, Cohen sends a warning that these data transformations should not be considered sufficient to protect individual’s privacy.

For years, computer science security and privacy researchers have sounded the alarm about the methods most often used to deidentify data, finding new attacks that can reidentify seemingly anonymized data points and proposing fixes. Yet these methods remain in common use, and held up as legally sufficient for fulfilling privacy-protection regulations such as HIPAA and GDPR.

“Policymakers care about real world risks instead of hypothetical risks,” Cohen said. “So people have argued that the risks security and privacy researchers pointed out were hypothetical or very contrived.”

While pursuing his PhD at MIT, Cohen set out to disprove this argument. The most common deidentification methods stem from an approach called k-anonymity, which transforms data just enough to make each individual indistinguishable from a certain number of other individuals in the data set. Cohen’s idea was that the very target of this deidentification method left it open to attack.

“The goal when you’re doing that sort of technique is to redact as little as you need to guarantee a target level of anonymity,” Cohen said. “But if you achieve that goal of redacting just as little as you need, then the fact that that’s the minimum might tell you something about what was redacted.”

!

Deidentification works by redacting quasi-identifiers – information that can be put together with data from a second source to de-anonymize a data subject. Failing to account for all possible quasi-identifiers can lead to disclosures. In [one famous example](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/), researchers took deidentified Netflix viewing data and combined it with data from the online movie review site IMDB, identifying users in the first data set by when they logged reviews of the movies they had recently watched.

Since these discoveries in the 2000s, policymakers have relied on experts to determine which aspects of a dataset are quasi-identifiers or not, to establish the bar for anonymity. Cohen tested the extreme – if every attribute is considered a quasi-identifier, do k-anonymity and its derivative techniques still work?

“If deidentification works at all, it should work when everything is quasi-identifying,” Cohen said. “That’s part of what makes this work powerful. It also means that the attacks work against almost all the techniques related to k-anonymity instead of any one specifically. The Netflix attack showed that it’s hard to say what is and isn’t a quasi-identifier. The downcoding attacks shows that, in certain settings, it doesn’t much matter.”

The paper describes two theoretical attacks and one real-world example that undermine the argument for these protections. The first, downcoding, reverse-engineers the transformations performed on the data, such as the zip code example mentioned earlier. The second attack uses downcoding for a predicate singling-out (PSO) attack, a specific type of attack against data anonymization standards under the European Union’s privacy law GDPR. That proof was important to show policymakers that k-anonymity is not sufficient for “publish-and-forget” anonymization under GDPR, Cohen said.

“The argument we’re making is against the idea that any of those techniques are sufficient to meet the legal bar of anonymization,” Cohen said. “We’re directly pushing back on that claim. Even by the regulatory standards, there’s a problem here.”

Cohen illustrated this insufficiency with a separate real-world demonstration on deidentified data from [edX](https://www.edx.org/), the popular massively open online course (MOOC) platform. By combining the dataset with data scraped from resumes posted to LinkedIn – information that would be trivially available to potential employers – Cohen could identify people who started but failed to complete edX courses, a potential violation of FERPA, the Family Educational Rights and Privacy Act. (edX was alerted to the flaw and has changed its data protections.)

The takeaway message, Cohen said, is that these deidentification methods are not a magic wand for waving away privacy concerns when sharing potentially sensitive data. He hopes that regulators will realize that a layered approach will be much more effective to achieve their goals.

“If what you want to do is take data, sanitize it, and then forget about it – put it on the web or give it to some outside researchers and decide that all your privacy obligations are done – you can’t do that using these techniques,” Cohen said. “They should not free you of your obligations to think about and protect the privacy of that data.”

Related

News

* [Campus NewsJul 05, 2023

  ## Sixteen UChicago faculty members receive named, distinguished service professorships](https://datascience.uchicago.edu/news/sixteen-uchicago-faculty-members-receive-named-distinguished-service-professorships/)
* [Campus NewsMar 20, 2024

  ## Assistant Professor Aloni Cohen Receives Prestigious Award for Groundbreaking Research in Machine Learning Complexity](https://datascience.uchicago.edu/news/assistant-professor-aloni-cohen-receives-prestigious-award-for-groundbreaking-research-in-machine-learning-complexity/)

## More on this topic

[!

DSI NewsApr 24, 2025

## DSI and The Patrick J. McGovern Foundation Invite the Next Generation to Imagine Data and AI for Good](https://datascience.uchicago.edu/news/dsi-and-the-patrick-j-mcgovern-foundation-invite-the-next-generation-to-imagine-data-and-ai-for-good/)
[!

DSI NewsFeb 13, 2025

## Transform Data Science and AI Accelerator Accepts 6 Startups into Latest Cohort](https://datascience.uchicago.edu/news/transform-data-science-and-ai-accelerator-accepts-6-startups-into-latest-cohort/)
[!

DSI NewsJan 29, 2025

## Illinois Makes History: How DSI’s Collaboration and Innovation Brought Broadband to 175,000 Underserved Locations](https://datascience.uchicago.edu/news/illinois-makes-history-how-dsis-collaboration-and-innovation-brought-broadband-to-175000-underserved-locations/)
[!

DSI NewsJan 28, 2025

## Summer Lab Research Program Expanded with NSF-Funded AI+Science REU Program](https://datascience.uchicago.edu/news/summer-lab-research-program-expanded-with-nsf-funded-aiscience-reu-program/)