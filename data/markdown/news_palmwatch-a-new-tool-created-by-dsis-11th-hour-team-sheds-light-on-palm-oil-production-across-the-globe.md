---
title: PalmWatch, a new tool created by DSI’s 11th Hour Project team, sheds light on palm oil production across the globe – DSI
original_url: https://datascience.uchicago.edu/news/palmwatch-a-new-tool-created-by-dsis-11th-hour-team-sheds-light-on-palm-oil-production-across-the-globe
category: news
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

DSI NewsFeb 22, 2024

# PalmWatch, a new tool created by DSI’s 11th Hour Project team, sheds light on palm oil production across the globe

PalmWatch, a new tool jointly created by DSI and Inclusive Development International, tracks deforestation by palm oil mills and connects that information to major, multinational brands’ sourcing

Palm oil is a required ingredient for a plethora of household products, from food items like packaged pastries and chips to cosmetics and soaps or even biofuels. But most palm oil is produced on mono-crop plantations, grown on huge tracts of land that were once tropical rainforests and other biodiverse ecosystems. Mapping the links between palm oil mills, multinational corporations, and future deforestation risk is a difficult data science problem to solve, but thanks to a partnership with [Inclusive Development International](https://www.inclusivedevelopment.net/) (IDI), the DSI used novel methods to solve this problem.

![PalmWatch heat map Guatemala](http://datascience.uchicago.edu/wp-content/uploads/2024/02/PalmWatch-Launch1-e1708628516355-600x482.png)

[Image: PalmWatch heat map Guatemala]

The DSI and the IDI, with support from the [11th Hour Project](https://11thhourproject.org/), launched a new tool called [PalmWatch](http://palmwatch.inclusivedevelopment.net) on February 22. Using rigorous data science and advanced, low-cost data visualization methods, PalmWatch traces palm oil supplies from the ground level, where the environmental and social impacts of palm oil cultivation occur, to the consumer brands that use the oil in their products.

“This launch of the PalmWatch tool has been a long time coming,” said Executive Director [David Uminsky](https://datascience.uchicago.edu/people/david-uminsky/) of the Data Science Institute at the University of Chicago. “We began this work with some very motivated graduate students as part of the [Data Science Clinic](https://datascience.uchicago.edu/education/data-science-clinic/), an experiential project-based course where students work as data scientists under the supervision of DSI staff and faculty. This has all the hallmarks of a great data science problem. We needed novel efforts to correctly undertake the spatial analysis and we needed to advance visualization methods under-the-hood to build the best interactive tool for the public.”

##### **PalmWatch connects data sources that were previously unlinked**

In an effort to increase transparency, multinational brands report the palm oil mills from which they source their material. However, creating a repository that sorts and organizes mills across the world requires collecting and standardizing this information. And even with this information, it takes additional computational methods to understand how each mill impacts local deforestation risks. DSI’s [11th Hour Project team](https://datascience.uchicago.edu/outreach/11th-hour-project/), led by Open Spatial Lab technical lead Dylan Halpern, had to contend with these challenges when they were building PalmWatch.

To connect these diverse data sets, they first had to scrape public disclosures from thirteen multinational consumer brands that show which mills these brands source from. This information then had to be standardized, with the palm oil mills geolocated on a searchable map. The data scientists also had to collect information about the mills, such as which companies own and operate them, which consumer brands they are affiliated with, and their [RSPO](https://rspo.org/) certification status (a metric measuring sustainability of palm oil production).

“Matching consumer brands’ disclosed mills with the authoritative list published by the World Resources Institute [as part of the standardization process] was quite a challenge,” said [Launa Greer](https://datascience.uchicago.edu/people/launa-greer/), a software engineer at the DSI. “Disclosures were typically located on obscure corners of the websites and difficult to scrape for information due to wildly-varying PDF layouts. After collecting the mill records, we linked them to those from the Universal Mill List using a combination of fuzzy string matching, distance approximations, and id joins to produce the final set of mills used for the site. We hope that making a clean, consolidated, and machine readable dataset of mills available to the public will accelerate similar supply-chain research efforts.”

![Maps of roads near palm oil mills](http://datascience.uchicago.edu/wp-content/uploads/2024/02/PalmWatch-Launch-e1708628361152-600x484.png)

[Image: Maps of roads near palm oil mills]

Colors represent where the road network can be most accessed by mills. Orange icons represent mill locations. Previous methods would not consider bridges or river crossings. Location near Sekadau, West Kalimantan, Indonesia.

In order to understand deforestation in the regions surrounding the mills, Greer and her colleagues drew a ‘catchment boundary’ around each mill, to show the approximate geographical area a mill is likely sourcing palm fruit from. The boundaries were limited by known geographical constraints like local roads and times estimates that the industry sets for fruit spoilage standards.

Combining these diverse data sets with catchment boundaries and then overlaying 20 years of deforestation data from the University of Maryland within each mill’s catchment area helped bring all these pieces into a complete picture. PalmWatch uses this data to assign a past deforestation score to each mill, based on the amount of forest cleared within its catchment area, along with a future deforestation risk score, based on past deforestation patterns and the amount of forest that remains at risk. This information is then connected to the brands sourcing from each mill, and can be aggregated and filtered, allowing users to see deforestation by brand, mill owner and mill corporate group.

“I’m very excited that this dashboard will be owned by local communities and nonprofits working in the space,” said Greer. “Previously, investigating the effects of palm oil supply chains was a laborious process; now groups will have analytics at their fingertips.”

##### PalmWatch is built with future-proofing in mind

Making sure that PalmWatch would be cheap to maintain and easy to update was a vital part of the process to ensure the website will continue to be a useful investigative tool. PalmWatch was built to be lightweight and not require heavy computation that can add up in costs to web hosts over time.

“Ongoing funding for community-centered data science projects is not always guaranteed, so it’s important to architect software that is cheap to own in the long term,” said DSI’s Open Spatial Lab technical lead [Dylan Halpern](https://datascience.uchicago.edu/people/dylan-halpern/). “It’s tragic to see fantastic software engineering and community-engaged data science fade away from public view due simply to a server bill.”

PalmWatch uses a “[baked data](https://simonwillison.net/2021/Jul/28/baked-data/)” model that runs analytics on three key outputs: company-mill relationships, mill impact data, and geospatial catchment areas. These are published through an API and use server-side rendering. Additionally, full data files are available for public download.

“We realized early on that palm oil production impacts each part of the world in a unique way; we integrated a collaborative content management system so that local advocates can add critical context, news, legal briefings, and other local knowledge to PalmWatch at every level – mill, country, consumer brand, and everything in between,” said Halpern.

When asked about ways that users can get engaged, he responded “If people are interested in contributing, they should absolutely contact Inclusive Development International at [palmwatch@inclusivedevelopment.net](mailto:palmwatch@inclusivedevelopment.net).”

The development team has future plans for additional updates, including a data pipeline github, a disclosure contribution guide, and plans to offer hands-on training to social impact organizations and journalists who want to dig deeper into specific data questions.

##### PalmWatch highlights the global risks of deforestation due to palm oil mills

The novel use of global palm oil mill data, combined with a global focus, is already bearing fruit. Users can view trends in PalmWatch at the country level, leading to new insights. Countries where palm oil production is not yet as common (or tracked as completely), such as Columbia or Honduras, have lower past deforestation scores overall, but higher future risk and some higher current deforestation. This indicates that future efforts might be needed in countries and regions where focus on deforestation due to palm oil cultivation hasn’t been featured prominently in advocates’ work.

When asked about how Palm Watch can provide insights for journalists, advocates, and other researchers, Uminsky responded, “PalmWatch is a model of innovation that we couldn’t have completed without IDI’s partnership and the support of the 11th Hour Project. We look forward to continuing development of this tool to meet the needs of its users and hope to lead future projects like this in the future.”

!!

Related

Insights

* [Data & SoftwareFeb 01, 2024

  ## DeBIT (Development Bank Investment Tracker)](https://datascience.uchicago.edu/insights/debit-development-bank-investment-tracker/)

News

* [DSI NewsDec 15, 2022

  ## New mBio Data Portal Brings Transparency to Genetically Modified Crops in Africa](https://datascience.uchicago.edu/news/new-mbio-data-portal-brings-transparency-to-genetically-modified-crops-in-africa/)
* [DSI NewsJan 09, 2023

  ## New DSI Open Spatial Lab Brings Expertise to Social Impact Organizations](https://datascience.uchicago.edu/news/new-dsi-open-spatial-lab-brings-expertise-to-social-impact-organizations/)
* [DSI NewsApr 15, 2024

  ## DSI Software Engineers create interactive map tool to maximize climate investment tax benefits](https://datascience.uchicago.edu/news/dsi-software-engineers-create-interactive-map-tool-to-maximize-climate-investment-tax-benefits/)
* [DSI NewsOct 07, 2024

  ## Bringing Transparency to Carbon Credit Projects](https://datascience.uchicago.edu/news/bringing-transparency-to-carbon-credit-projects/)
* [DSI NewsOct 29, 2024

  ## Supporting Indigenous Data Sovereignty and Voter Education with North Dakota Native Vote](https://datascience.uchicago.edu/news/supporting-indigenous-data-sovereignty-and-voter-education-with-north-dakota-native-vote/)

* [DSI NewsApr 24, 2025

  ## DSI and The Patrick J. McGovern Foundation Invite the Next Generation to Imagine Data and AI for Good](https://datascience.uchicago.edu/news/dsi-and-the-patrick-j-mcgovern-foundation-invite-the-next-generation-to-imagine-data-and-ai-for-good/)

1 of 1

+ Show All
- Show Less

## More on this topic

[!

In The MediaMay 06, 2024

## Nūtrad, from Transform Cohort 2, featured in The Chicago Maroon](https://datascience.uchicago.edu/news/nutrad-from-transform-cohort-2-featured-in-the-chicago-maroon/)
[![2024 Winter Community Data Fellows, with program manager Ari Zickau](https://datascience.uchicago.edu/wp-content/uploads/2024/04/IMG_20240304_135726-scaled-e1713977769618-750x500.jpg)

[Image: 2024 Winter Community Data Fellows, with program manager Ari Zickau]

DSI NewsApr 18, 2024

## Community Data Fellow Stephania Tello Zamudio helps broaden internet access for Illinois residents](https://datascience.uchicago.edu/news/community-data-fellow-stephania-tello-zamudio-helps-broaden-internet-access-for-illinois-residents/)
[!

DSI NewsApr 15, 2024

## DSI Software Engineers create interactive map tool to maximize climate investment tax benefits](https://datascience.uchicago.edu/news/dsi-software-engineers-create-interactive-map-tool-to-maximize-climate-investment-tax-benefits/)
[!

DSI NewsSep 14, 2023

## DSI Summer Lab Students Present Wide-Ranging Research](https://datascience.uchicago.edu/news/dsi-summer-lab-students-present-wide-ranging-research/)