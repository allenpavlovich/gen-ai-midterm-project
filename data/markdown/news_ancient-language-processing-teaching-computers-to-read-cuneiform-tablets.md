---
title: Ancient Language Processing: Teaching Computers to Read Cuneiform Tablets – DSI
original_url: https://datascience.uchicago.edu/news/ancient-language-processing-teaching-computers-to-read-cuneiform-tablets
category: news
date: 2025-05-04
---

!

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

DSI NewsFeb 12, 2020

# Ancient Language Processing: Teaching Computers to Read Cuneiform Tablets

A CDAC-funded collaboration between researchers from the UChicago Oriental Institute and the Department of Computer Science applies modern computer vision approaches to read ancient cuneiform tablets.

Twenty-five centuries ago, the “paperwork” of the Achaemenid Empire in Persia was recorded on clay tablets. In 1933, archeologists from the University of Chicago’s Oriental Institute (OI) found tens of thousands of these tablets at an excavation site in Persepolis, located in modern-day Iran. For decades, researchers studied and translated these ancient documents “by hand,” revealing rich information about Achaemenid history, society, and language. 

But this manual deciphering process is very difficult, slow, and prone to errors. Since the 1990’s, scientists have attempted to recruit computers to help, with limited success due to the three-dimensional nature of the tablets and the complexity of the cuneiform characters. But recent leaps forward in computer vision and language processing may finally make automated transcription of these tablets possible, freeing up archeologists for higher-level analysis.

That’s the motivation behind DeepScribe, a CDAC-funded collaboration between researchers from the OI and the Department of Computer Science. With a training set of more than 6,000 annotated images from the [Persepolis Fortification Archive](https://oi.uchicago.edu/research/projects/persepolis-fortification-archive) (directed by professor emeritus [Matthew W. Stolper](https://nelc.uchicago.edu/people/matthew-w-stolper)), the project will build a model that can “read” as-yet-unanalyzed tablets in the collection, and potentially a tool that archeologists can adapt to other studies of ancient writing.

“If we could come up with a tool that is flexible and extensible, that can spread to different scripts and time periods, that would really be field-changing,” said [Susanne Paulus](https://nelc.uchicago.edu/faculty/paulus), Associate Professor of Assyriology at the University of Chicago and Tablet Collection Curator at the OI. 

!

Hotspots outlining cuneiform signs on an Elamite tablet from the Persepolis Fortification Archive

The collaboration was sparked when Paulus, Sandra Schloen, and Miller Prosser of the OI met UChicago CS Assistant Professor [Sanjay Krishnan](http://sanjayk.io/) at [a Neubauer Collegium event on digital humanities](https://neubauercollegium.uchicago.edu/faculty/an_organon_for_the_information_age/). Schloen and Prosser oversee [OCHRE](https://voices.uchicago.edu/ochre/help/about/), a database management platform supported by the OI to capture and organize data from archeological excavations and other forms of research. Krishnan applies deep learning and AI techniques to data analysis, including video and other complex data types. The overlap was immediately apparent to both sides.

“From the computer vision perspective, it’s really interesting because these are the same challenges that we face. Computer vision over the last five years has improved so significantly; ten years ago, this would have been hand wavy, we wouldn’t have gotten this far,” Krishnan said. “It’s a good machine learning problem, because the accuracy is objective here, we have a labeled training set and we understand the script pretty well and that helps us. It’s not a completely unknown problem.”

That training set is thanks to over 80 years of close study by OI and UChicago researchers and a recent push to digitize high-resolution images of the tablet collection — currently over 60 terabytes and still growing — before their [return to Iran](https://apnews.com/64c8088618704acfb4fcb29821ee82e2). Using this collection, researchers created a dictionary of the Elamite language inscribed on the tablets, and students learning how to decipher cuneiform built a database of more than 100,000 “hotspots,” or identified individual signs. 

!

Image hotspot cutouts representing instances of the cuneiform sign for “3”

With resources from the [UChicago Research Computing Center](http://rcc.uchicago.edu), Krishnan (and interested former student of cuneiform and now west-coast engineer, Eddie Williams) used this annotated dataset to train a machine learning model, similar to those used in other computer vision projects. When tested on tablets not included in the training set, the model could successfully decipher cuneiform signs with around 80 percent accuracy. Ongoing research will try to nudge that number higher while examining what accounts for the remaining 20 percent. 

But even 80 percent accuracy can immediately provide help for transcription efforts. Many of the tablets describe basic commercial transactions, similar to “a box of Walmart receipts,” Paulus said. And a system that can’t quite make up its mind may still be useful.  

“If the computer could just translate or identify the highly repetitive parts and leave it to an expert to fill in the difficult place names or verbs or things that need some interpretation, that gets a lot of the work done,” Paulus said. “And if the computer can’t make a definitive decision, if it could give us back probabilities or the top four ranks, then an expert has a place to start. That would be amazing.”

Even more ambitiously, the team imagines DeepScribe as a general-purpose deciphering tool that they can share with other archeologists. Perhaps the model can be retrained for cuneiform languages other than Elamite, or can make educated suggestions about what text was written on missing pieces of incomplete tablets. A machine learning model might also help determine the origin of tablets and other artifacts of unknown provenance, a task currently addressed by chemical testing.

By joining the CDAC Discovery Grant cohort, the DeepScribe team can connect with other projects using computer vision approaches for applications such as [studying biodiversity in marine bivalves](/research/exploring-climate-and-biodiversity-with-3d-deep-learning/) and [disentangling style from content in artistic work](/research/disentangling-visual-style-and-content/). The collaboration also hopes to inspire future partnerships between the OI and UChicago CS, as digital archeology increasingly intersects with advanced computational approaches.

“I think it helped something that would have ended at a dinner conversation become an actual collaboration,” Krishnan said. “It got us to do more than talking.”

Related

Research

* [Discovery Grant

  ## Deciphering Cuneiform with Artificial Intelligence](https://datascience.uchicago.edu/research/deciphering-cuneiform-with-artificial-intelligence/)

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

DSI NewsJan 28, 2025

## Summer Lab Research Program Expanded with NSF-Funded AI+Science REU Program](https://datascience.uchicago.edu/news/summer-lab-research-program-expanded-with-nsf-funded-aiscience-reu-program/)