---
title: The Challenging Path to Internet Broadband Access Equity – DSI
original_url: https://datascience.uchicago.edu/insights/the-challenging-path-to-internet-broadband-access-equity
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogAug 29, 2024

# The Challenging Path to Internet Broadband Access Equity

Jonatas Marques, Data Science Institute Postdoctoral Fellow

Access to the Internet—much like energy, water, and sanitation—is essential. People rely on the Internet for work, entertainment, education, health care, and more. Despite the Internet’s prominence in the US economy, barriers in access and adoption still persist across the nation. In response to persistent gaps in the diffusion of high-speed, reliable broadband, and to help close gaps in access and achieve the goal of universal service across the United States (US), the US Federal Government allocated significant investments for the expansion of broadband as part of the [Infrastructure Investment and Jobs Act (IIJA)](https://www.whitehouse.gov/briefing-room/statements-releases/2021/08/02/updated-fact-sheet-bipartisan-infrastructure-investment-and-jobs-act/). The [Broadband Equity, Access, and Deployment (BEAD)](https://www.internetforall.gov/program/broadband-equity-access-and-deployment-bead-program) program provides more than $42 billion to expand high-speed Internet access across the country through planning, infrastructure deployment, and adoption programs.

In order to determine how to distribute BEAD funds among states and territories, the Federal Communications Commission (FCC) was assigned to collect and visualize Internet coverage data through the [National Broadband Map](https://broadbandmap.fcc.gov/) (NBM). This map contains availability data compiled from Internet Service Providers (ISPs) regarding their broadband offerings to depict fixed Internet access availability for every location in the country. Depending on the maximum available download and upload speeds offered in a particular location, that location is considered either unserved (only speeds under 25 and 3 Mbps are offered), underserved (no access offerings at or above 100/20 Mbps), or served (access to 100/20 Mbps or higher speeds). The status of each location, as shown in the map, determines its eligibility to receive funds from the BEAD program, with only unserved and underserved locations being considered eligible. Further, the spatial distribution of BEAD-eligible locations will determine the proportion of funding communities will receive to address broadband inequities.

Given the importance of the broadband map, the FCC has made a historic call for engagement from citizens to make the data it contains accurately reflect the lived reality of broadband consumers. Citizens and organizations were tasked with checking the reported availability at their familiar locations (e.g., households, workplaces) and raising challenges refuting the status of availability whenever the map did not match their lived experience. As part of this effort to continually improve the broadband map, the FCC has also regularly published data reporting submitted challenges (e.g, their associated locations, providers, access technologies, and reasons for challenge) as well as their outcomes (i.e., upheld, overturned, or withdrawn).

!

Fig 1. Percentage of broadband-serviceable locations (BSLs) with at least one submitted challenge per US state or territory. Nebraska had strong participation in the challenge process, followed by Virginia, New Mexico, and Maine. Most states and territories have low participation rates.

My colleagues and I at the Internet Equity Initiative have been investigating how different states, counties, and communities have participated in the challenge process, where they were successful and where they were not, where they focused on specific types of access technology (e.g., cable, fiber, fixed wireless), submitted challenges due to specific reasons, and more. In this post, we summarize our main findings to date. Since the start of the challenge process in late 2022, more than 3.6 million challenges have been submitted with about 70% of them being upheld by the FCC, resulting in changes to the broadband map. These challenges are distributed among more than 2.8 million distinct locations. Considering that the US has an estimated 120 million unique broadband-serviceable locations, those with at least one challenge represent only about 2.3% of all locations. This percentage points to an overall low participation rate that is pervasive among most states and territories (See Figure 1). The state of Nebraska is the main exception, with about 75% of locations engaging in the challenge process and more than nine hundred thousand challenges submitted. Other states with significant participation were Virginia, New Mexico, and Maine with about 22%, 18%, and 15% of all locations having submitted at least one challenge, respectively. Looking more closely at Nebraska, we found that 97% of challenges were submitted against fixed wireless providers. Considering the country as a whole, more than half of all challenges were also against providers for this type of Internet access. This suggests [very](https://www.latimes.com/business/story/2023-02-16/fcc-investigates-broadband-providers-coverage-claims) [frequent](https://arstechnica.com/tech-policy/2024/02/isps-keep-giving-false-broadband-coverage-data-to-the-fcc-groups-say/) [overstatement](https://www.cnet.com/home/internet/fcc-reportedly-investigating-if-internet-providers-exaggerated-coverage/) of coverage by Internet providers offering fixed wireless Internet access.

!

Fig 2. Percentage of broadband-serviceable locations with at least one submitted challenge per county. Nebraska has high participation throughout. Many counties in the central continental area have not submitted any challenges.

We also analyzed how participation in the challenge process is distributed within states and territories (See Figure 2). We were curious to observe whether challenges were well distributed among counties within a state or if there is a concentration of participation in certain areas. One important insight from this analysis is the presence of a large swath of counties in the central continental area, from north to south, where there were no challenges submitted at all. Interestingly, Nebraska, the state with the most engagement, is situated right in the middle of this swatch. This contrast between Nebraska and other central continental states could suggest major underreporting of inaccuracies in this area. For Nebraska, we also observe that participation levels are reasonably high and homogeneous across the state. We also observe that most states have low and homogeneous levels of participation. Finally, we note that a few states (e.g., Virginia, New, York, Illinois, Florida) present small pockets of counties with expressive participation alongside low participating counties. For Illinois, the center-west counties of Pike, Calhoun, Scott, Greene, and Morgan had the most engagement in the challenge process, ranging between 40% and 80%.

A major finding from this exploration is that levels of participation are not homogeneous but rather vary across the US. This raises an important question; what factors strongly influenced participation in the challenge process? To answer this question and others, we are in the process of exploring demographic indicators such as race, income, education, age, and rurality and how these factors relate to participation in the challenge process. Based on preliminary results, we note that there may be hidden forces at play that data analysis alone cannot identify. As next steps, we envision examining policy decisions made by state broadband offices when engaging with the process (e.g., widespread public campaigns, special task forces), exploring the existence of patterns in availability reporting by ISPs that lead to challenges, and understanding the barriers to raising successful challenges.

Related

Insights

* [Data & SoftwareJan 02, 2024

  ## IEI Tackles Broadband Equity through Bead Speed Challenges](https://datascience.uchicago.edu/insights/iei-tackles-broadband-equity-with-the-bead-challenge/)

News

* [DSI NewsMay 09, 2022

  ## Digital Divide: Data Highlights Internet Inequities in Chicago](https://datascience.uchicago.edu/news/digital-divide-data-highlights-internet-inequities-in-chicago/)
* [DSI NewsJun 09, 2022

  ## Nick Feamster Talks Internet Equity on Light Reading Podcast](https://datascience.uchicago.edu/news/nick-feamster-talks-internet-equity-on-light-reading-podcast/)
* [In The MediaJan 05, 2023

  ## Prof. Nicole Marwell Discusses Internet Equity on Chicago Tonight](https://datascience.uchicago.edu/news/prof-nicole-marwell-discusses-internet-equity-on-chicago-tonight/)
* [DSI NewsJan 29, 2025

  ## Illinois Makes History: How DSI’s Collaboration and Innovation Brought Broadband to 175,000 Underserved Locations](https://datascience.uchicago.edu/news/illinois-makes-history-how-dsis-collaboration-and-innovation-brought-broadband-to-175000-underserved-locations/)

+ Show All
- Show Less

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
[!

BlogJul 29, 2024

## Does Political Polarization Really Undermine Democracy? Maybe Not](https://datascience.uchicago.edu/insights/does-political-polarization-really-undermine-democracy-maybe-not/)