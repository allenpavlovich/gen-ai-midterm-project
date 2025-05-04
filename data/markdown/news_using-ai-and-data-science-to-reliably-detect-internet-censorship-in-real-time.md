---
title: Using AI and Data Science to Reliably Detect Internet Censorship in Real Time – DSI
original_url: https://datascience.uchicago.edu/news/using-ai-and-data-science-to-reliably-detect-internet-censorship-in-real-time
category: news
date: 2025-05-04
---

!

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

DSI NewsNov 02, 2021

# Using AI and Data Science to Reliably Detect Internet Censorship in Real Time

A new project brings together researchers from the UChicago Data Science Institute, Princeton, and SRI International to build new AI and data science tools that monitor and detect Internet censorship with greater levels of confidence.

While the Internet has proven a powerful force for freedom, controlling the flow of online traffic is one of the most powerful methods used by 21st century totalitarian governments. By blocking or throttling areas of the Internet, a nation-state can slow or even entirely cut off the spread of information, or prevent the use of applications and tools it considers dangerous or threatening to its rule. But for obvious reasons, these governments involved do not advertise their activities, making it hard to detect these restrictions.

A new multi-institutional study led by University of Chicago Professor [Nick Feamster](https://people.cs.uchicago.edu/~feamster/) will build new AI and data science tools to monitor and detect Internet censorship, develop new statistical techniques to identify censorship with greater levels of confidence, and ultimately create a “weather map” for certain types of nation-state interference and control of online information. The $1 million grant, funded by the U.S. Defense Advanced Research Projects Agency (DARPA), brings together researchers from the [UChicago Data Science Institute](http://datascience.uchicago.edu) (DSI), Princeton University, and [SRI International](https://www.sri.com/).

“Our goal is to increase our levels of confidence about what is being censored, when censorship occurs, and where it is being censored,” said Feamster, Neubauer Professor of Computer Science and Director of Research for the Data Science Institute. “Our past work on measuring Internet censorship has developed tools to identify *possible* instances of censorship, but the measurements have some amount of uncertainty, and thus we need to develop more robust statistical techniques. We also aim to derive and provide real-time insights from that data—another significant data science challenge since the scope and scale of the Internet is so massive.”

The Internet is a global network of computers, and when governments want to interfere with or block information from entering their borders, they can do so at different “levels” of that network. By inserting firewalls, middleboxes, and other intermediary devices on the path into and out of their countries, authorities can interfere with traffic in a variety of ways, such as blocking or throttling websites or pages, such as news sites, online forums, or social media platforms. An authority could block a site or a page outright, or simply slow access to the point of being no longer usable. 

Because Internet slowdowns and failures happen during the course of normal operations, distinguishing censorship from “normal” outages or slowdowns is a difficult task. But the massive amounts of data moving through the global network of the Internet contains subtle clues that this interference is happening, and because intentional slowdowns look different from “normal” ones, there is hope that AI can detect the difference. Feamster’s group will train new AI models and apply novel data science techniques to detect the “fingerprints” of these devices, giving internet watchdogs, policymakers, and citizen groups the ability to observe when and where censorship is happening.

!

Nick Feamster, Faculty Director of Research at the Data Science Institute.

The research will build off of tools Feamster has previously developed that use network traffic to better measure speed and performance of home Internet connections. His Net Microscope tool was [used in a *Wall Street Journal* investigation](https://cdac.uchicago.edu/news/nick-feamsters-research-drives-wall-street-journal-investigation-of-streaming-video/) of whether more expensive Internet plans truly provide better streaming speeds for apps such as Netflix and Zoom. Through the [Internet Access & Equity Initiative](https://datascience.uchicago.edu/research/mapping-and-mitigating-the-urban-digital-divide/), a project of the Data Science Institute funded by [data.org](http://data.org), Feamster leads a team using similar tools to measure access to high-speed broadband in different areas of Chicago.

Though the motivation is different, some of the same methods apply in sifting through network traffic for signs of censorship.

“Detecting Internet censorship at scale is a challenging Internet measurement problem, not unlike those we have tackled in the areas of network performance measurement and diagnosis,” Feamster said. “In both cases, the raw data is similar: we’re effectively measuring properties of a network path or endpoint and looking for unusual performance or behavior. In the case of performance measurement, we’re looking for problems that result from benign causes, such as a misconfiguration or underprovisioning. Detecting censorship involves looking for similar types of anomalies—with the difference being that the disruptions and degradations are introduced intentionally.”

The project will start by training models using data gathered by SRI, as well as other existing projects that have gathered large amounts of data, including the [Tor Project](https://www.torproject.org/) and the [Censored Planet](https://censoredplanet.org/) project at the University of Michigan. The initial phases of the project will involve training models to detect anomalous activity by scanning through terabytes of data containing both normal and censored Internet traffic. The researchers will also conduct laboratory studies with firewall and middlebox devices to fingerprint these devices and also to generate training data to help discover the presence of these devices across the Internet.

“We want to know, ‘What does traffic look like when these devices are manipulating traffic in various ways?’,” Feamster said. “If we can fingerprint them using some of the tools that we’ve developed through other projects, then we can get better labeled data sets, so that when we see weird things in the wild, hopefully there’s a better chance that we’ve already seen them in a lab setting and know what they are.”

At the end of the project, the researchers plan to deliver new monitoring tools and dashboards to consumers of the data—who might be diplomats, policymakers, or even regular citizens. Feamster envisions a real-time “weather map” for censorship, where observers can almost immediately see Internet interference as it is happening, in which countries, and even what sites or content governments are manipulating. The information could have a range of applications, from informing citizens, diplomats, and policymakers about the existence of censorship, to inspiring the designs of the next generation of tools to circumvent these forms of information controls.. 

“This research, which aims to reliably discover Internet censorship at scale, in real-time, develops critical capabilities for allowing citizens around the world to live in a free and open society, to promote constructive discourse, and ultimately to allow communities, societies, and public institutions to thrive,” Feamster said. “It is a quintessential data science problem—to date, computer scientists have developed specific Internet measurement techniques as building blocks, but those techniques also still yield messy data, with a lot of uncertainty. Data science allows us to take these fundamental approaches and ultimately go from messy data to deriving insights with more confidence that we can today.”

[Image created by Caroline Madigan for opensource.com, view original on [Flickr](https://www.flickr.com/photos/47691521@N07/6554315319)]

## More on this topic

[!

DSI NewsApr 24, 2025

## DSI and The Patrick J. McGovern Foundation Invite the Next Generation to Imagine Data and AI for Good](https://datascience.uchicago.edu/news/dsi-and-the-patrick-j-mcgovern-foundation-invite-the-next-generation-to-imagine-data-and-ai-for-good/)
[!

DSI NewsApr 22, 2025

## The University of Chicago Data Science Institute and Google Partner on Cutting-Edge AI and Security Research](https://datascience.uchicago.edu/news/the-university-of-chicago-data-science-institute-and-google-partner-on-cutting-edge-ai-and-security-research/)
[!

DSI NewsFeb 13, 2025

## Transform Data Science and AI Accelerator Accepts 6 Startups into Latest Cohort](https://datascience.uchicago.edu/news/transform-data-science-and-ai-accelerator-accepts-6-startups-into-latest-cohort/)
[!

DSI NewsJan 29, 2025

## Illinois Makes History: How DSI’s Collaboration and Innovation Brought Broadband to 175,000 Underserved Locations](https://datascience.uchicago.edu/news/illinois-makes-history-how-dsis-collaboration-and-innovation-brought-broadband-to-175000-underserved-locations/)