---
title: The Language of Policing: Does It Say More Than We Think? – DSI
original_url: https://datascience.uchicago.edu/news/the-language-of-policing-does-it-say-more-than-we-think
category: news
date: 2025-05-04
---

!

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

DSI NewsApr 16, 2020

# The Language of Policing: Does It Say More Than We Think?

A CDAC Discovery Grant project uniting researchers from UChicago and the Toyota Technological Institute at Chicago builds a new machine learning pipeline to transcribe police communications and better understand the role of language in officer-public interactions.

In recent years, a host of data-driven efforts have attempted to improve policing, decrease crime, and prevent incidents between officers and the public. But one rich source of data remains unmined: police radio communications. The language used by police officers on their radios is highly structured, meant to convey information as accurately and efficiently as possible. But subjectivity, emotions, and other complicating factors can creep into these conversations between officers and dispatchers, perhaps influencing how high-pressure incidents are handled.

[Margaret Beale Spencer](https://humdev.uchicago.edu/directory/margaret-beale-spencer), the Marshall Field IV Professor of Urban Education and Life Course Development at the University of Chicago, believes that this language could provide a window into the broader relationship between police officers and minority youth. Yet in order to open that window, technical advances are first needed to accurately convert noisy, low quality audio recordings into text and other features for research and analysis. Those challenges led to a collaboration with language processing expert [Karen Livescu](https://ttic.uchicago.edu/~klivescu/), Associate Professor at the [Toyota Technological Institute at Chicago](https://www.ttic.edu/), and [a CDAC-funded seed project](/research/a-data-processing-pipeline-for-police-communications/) in the Winter 2019 round of funding.

Using a public archive of more than 45,000 hours of recordings from Chicago police radio bands, the team will build a data processing pipeline that transcribes audio and reconstructs specific events — from routine arrests to officer-involved shootings — in order to better understand the institutional, individual, and contextual factors that influence policing incidents.

“We’re using an innovative strategy which focuses on language produced between dispatchers and police officers, and police officers with each other,” Spencer said. “We’re looking at the language officers use because we know that language is powerful; thus, getting it right matters given unavoidable consequences for interpersonal encounters and relationships. Similarly, in terms of young people and the training of officers, we want officers to understand the normal human development of youngsters, who are at a point in their own lives during which they struggle with identity issues and seek to fulfill emotional needs, as well. Thus, it’s a different approach that we’re very excited about which has important implications for police training. We believe it has great potential for improving encounters between police officers and minority youth.”

## The Influence of Language

The procedural language and code system used by officers and dispatchers is rich with information about the time and location of incidents, the units responding, and how individuals on the scene interpret the situation in real time. Unlike police reports written after the fact that can be distorted by memory, hindsight, or other factors, the audio is also “pre-reflective,” and thus can potentially provide a more direct view of the preconceptions officers bring to interactions.

For example, said Christopher Graziul, a data scientist on the project, an officer may choose to describe a crowd of people as “excited” or “agitated.” In combination with other factors, such as the location of the disturbance and officers’ previous experience with that neighborhood, these word choices could impact the orientation or the response of officers without basis, leading to inaccurate risk assessments and/or unnecessary escalations.

“The idea is how we communicate about things really affects how we think about situations that we enter,” Graziul said. “Language is something that we build up over time. And as much training as you get to make the procedural language standardized, there will always be adaptations and different ways of describing the same kind of encounter based on your own experience.”

The first step will be creating the pipeline for how to convert audio data — gathered from an online archive — into machine readable text, metadata, and finally, reconstructions of discrete incidents. In addition to information about the time, location, and participants in each event, the researchers hope to extract acoustic features that can indicate the emotions or stress level of those involved. 

But creating that dataset will require more than the standard, off-the-shelf machine learning and speech recognition tools. The raw recordings are extremely noisy, and present challenges in accurate transcription, identification of different speakers, and separation of concurrent events into discrete incidents.

“Modern automatic speech recognition works well when it is trained on large amounts of data matching the domain of interest,” Livescu said. “The domain of police radio communications differs from typical training data in multiple ways, including the extreme background noise, high-stress speech, and the linguistic content itself. Human listeners can take educated guesses when the audio is degraded, based on their knowledge of the domain and context. So the challenge here is teaching a speech recognizer to adapt to this context, and to collect and annotate enough of our own data to do so.”

## A Conversation Starter

Once assembled, the project will make the data open and available to other researchers, after scrubbing it for personally identifiable information. Spencer’s group plans to use the data in their research on life course human development and minority youth, to better understand the communication between law enforcement officials and young people.

“The second component is understanding the mechanisms and processes behind these actual encounters, and we know we can only understand those through talking to people,” Graziul said. “So we want to interview officers, we want to interview youth, we want to understand what kind of factors inform their orientation toward each other. Then use that information to understand the patterns that we initially find in the data, and develop training.”

“By interviewing police officers, we can get a sense of the degree to which they identified with the youngsters they encounter. This is really important, because when you’re under stress and in the moment trying to adapt to the situation, the degree to which you can identify with the other person really matters,” Spencer said. “I take pride in the fact that we are viewing both police officers as well as our youth as humans coping during highly stressful situations.”

Related

Research

* [Project

  ## A Data Processing Pipeline for Police Communications](https://datascience.uchicago.edu/research/a-data-processing-pipeline-for-police-communications/)

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