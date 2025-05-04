---
title: Using Computer Vision to Study Chicago Neighborhoods – DSI
original_url: https://datascience.uchicago.edu/insights/using-computer-vision-to-study-chicago-neighborhoods
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogMay 01, 2024

# Using Computer Vision to Study Chicago Neighborhoods

Riley Tucker, Data Science Institute Postdoctoral Fellow

Social scientists have [long theorized](https://nij.ojp.gov/library/publications/crime-prevention-through-environmental-design-and-community-policing) that people behave differently depending on how they see their environment. Within my field of criminology, scholars have argued that people have greater ability to take action against crime (calling 911, verbally admonishing a perpetrator, etc.) when they can easily see the objects present in their environment. For example, homeowners are more easily able to detect would-be burglars if the sight-lines from their windows are not obscured by trees. From the same theoretical perspective, it has been argued that people are more motivated to actively respond to crime when they live in an area they perceive to be aesthetically pleasing. Although social scientists have had a lot of ideas about how visual features of places impact behavior, visual features have historically been challenging to measure, making it hard to test such ideas. To address this problem, I have been working with my colleagues in the [*Environmental Neuroscience Lab*](https://voices.uchicago.edu/bermanlab/) to develop computer vision AI models that can “look” at Google Streetview images to tell us about the presence of visual cues that may alter the way people behave.

##### *Measuring Perceptions of Urban Visuals*

To train an AI model to look at an image and tell us the information important to us, we need to give it some information about what to look for. For example, if we want to develop a model that can look at an urban image and tell us how easy it is to see through the environment, we need to show it images with varying levels of environmental transparency so the model knows how to interpret the tested images. To create a “training dataset” our AI can learn from, we have created a *FastRating Image Task* where research participants are shown a grid of Google Streetview images and asked to select the 4 images where they can most easily “see or perceive what’s going on inside of the buildings.” By repeatedly testing image stimuli with many participants, we can rank images across Chicago in terms of their environmental transparency.

##### *Measuring Neighborhoods Visually*

While this fast rating task gives us insight into how people perceive visual features such as environmental transparency, it would be unfeasible to have humans rate all 200,000 of the Google Streetview images we have collected across Chicago. As such, we can instead take our smaller sample of human-rated images and show them to a computer vision AI to develop a [ResNet-50-based model](https://datagen.tech/guides/computer-vision/resnet-50/) that can look at any Google Streetview image and assign it an environmental transparency score.

!

The FastRating Image Task asks respondents to quickly identify images meeting certain criteria. In this example, the user is being asked to identify images featuring environmental transparency.

Because each image has an associated GPS coordinate, we are able to identify which neighborhood each image comes from. By averaging scores of images within the same neighborhood, we can then create city-wide neighborhood maps of visual features such as environmental transparency. In the map below, we can see that Chicago’s Loop and North Side neighborhoods, with many densely compacted buildings, tend to have less environmental transparency compared to the rest of Chicago. Sightlines then tend to open up as we move away towards the city’s outskirts and into the suburbs.

!

By averaging AI-assigned environmental transparency scores over many images from the same area, we can create neighborhood measures of environmental transparency. In this map, greener areas are more transparent while areas in purple are less transparent.

##### *Understanding Crime & Behavior*

Given that there appears to be a great difference in urban visual features across Chicago neighborhoods, we investigated whether these visual features explain differences in behaviors or social outcomes across communities. By connecting our neighborhood data on visual features to neighborhood crime [data provided by the Chicago Police Department](https://data.cityofchicago.org/Public-Safety/Crimes-2022/9hwr-2zxp/data), we evaluated if places with certain types of visual features tend to experience more crime. Using [*structural equation models*](https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/structural-equation-modeling/) that allowed us to assess how different neighborhood features lead to crime, we found that neighborhoods that were more visually transparent and aesthetically pleasing tended to experience less violent and non-violent crime even when controlling for residential demographic features associated with crime such as economic disadvantage and segregation.

In the next stage of our research, we are interested in measuring these visual features over time to more directly test if people change their behavior based on the visual cues in their environment. Because our approach allows us to train computer vision models for any visual feature of our choosing, we are excited to broaden our scope to think about how visual features of places more broadly alter the way people think and behave across urban contexts.

## More on this topic

[!

BlogMar 13, 2025

## Data Ecology Faculty Co-Director Bridget Fahey Writes About Congressional Authority Over Government Data](https://datascience.uchicago.edu/insights/data-ecology-faculty-co-director-bridget-fahey-writes-about-congressional-authority-over-government-data/)
[!

BlogFeb 26, 2025

## Federal budget cuts threaten to decimate America’s AI superiority—and other countries are watching](https://datascience.uchicago.edu/insights/federal-budget-cuts-threaten-to-decimate-americas-ai-superiority-and-other-countries-are-watching/)
[![Fig 1. Percentage of broadband-serviceable locations (BSLs) with at least one submitted challenge per US state or territory. Nebraska had strong participation in the challenge process, followed by Virginia, New Mexico, and Maine. Most states and territories have low participation rates.](https://datascience.uchicago.edu/wp-content/uploads/2024/08/Fig1-750x500.png)

[Image: Fig 1. Percentage of broadband-serviceable locations (BSLs) with at least one submitted challenge per US state or territory. Nebraska had strong participation in the challenge process, followed by Virginia, New Mexico, and Maine. Most states and territories have low participation rates.]

BlogAug 29, 2024

## The Challenging Path to Internet Broadband Access Equity](https://datascience.uchicago.edu/insights/the-challenging-path-to-internet-broadband-access-equity/)
[!

BlogJul 29, 2024

## Does Political Polarization Really Undermine Democracy? Maybe Not](https://datascience.uchicago.edu/insights/does-political-polarization-really-undermine-democracy-maybe-not/)