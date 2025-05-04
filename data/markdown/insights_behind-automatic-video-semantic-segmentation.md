---
title: Behind Automatic Video Semantic Segmentation – DSI
original_url: https://datascience.uchicago.edu/insights/behind-automatic-video-semantic-segmentation
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogJun 06, 2024

# Behind Automatic Video Semantic Segmentation

Chong Liu, Data Science Institute Postdoctoral Fellow

Imagine a robot cleaning your house, a tractor working in a farm field without a farmer, or a self-driving car taking you to the airport. You may wonder how the AI systems in each of these examples navigate in these scenarios. This is a critical question, because the AI system needs to understand the environment (ex., streets, pedestrians) and tasks (driving) such that proper actions (move forward / turn left) can be taken.

In practice, the AI system relies on a computer vision model that can automatically generate semantic labels for each video pixel, which is known as automatic video semantic segmentation. For example, it helps self-driving cars understand what they’re seeing as they drive. Here’s how it works:

1. Capture Video: The car has cameras that record everything around it as it moves.
2. Prepare the Video: The car’s computer cleans up the video to make it clearer and easier to analyze.
3. Learn to See: The computer is trained using lots of annotated videos, where each part of the video is marked as street, car, person, etc. This helps the computer learn to recognize these things on its own. The figure below shows a video frame example.
4. Identify Objects: When the car is driving, the computer looks at each frame of the video and identifies every pixel as part of the street, a car, a person, etc. This creates a map of everything around the car.
5. Keep it Smooth: The computer uses special techniques to make sure its understanding of the scene is consistent from one frame to the next, avoiding the perception of flickering or jumping objects.
6. Make Decisions: The car uses this detailed map to make decisions, like when to stop, go, or turn, ensuring it can navigate safely and avoid obstacles.

!

A video frame example from [Cityscape dataset](https://www.cityscapes-dataset.com/) where different colors denote different labels in pixel level. For example, red means person and light blue means sky.

The key step in this whole process is step 3: Learn to See. How can we train an AI model that is able to precisely make predictions on all pixels in all video frames? It sounds challenging in practice, but isn’t entirely impossible.

In order to  successfully train a computer,    we need lots of accurately annotated videos. Unfortunately, it’s usually impossible to ask a human annotator to fully label an entire video sequence due to the high per-pixel annotation cost. Therefore, the annotations are usually limited to a small subset of the video frames to save on this cost.

However, are all video frames equally important to get annotated for training purposes? Not really!

From the point of view of machine learning, this kind of problem falls into the framework of [active learning](https://en.wikipedia.org/wiki/Active_learning_(machine_learning)), where the algorithm interacts with a human annotator for multiple rounds. At each round, the algorithm can strategically select a video frame and send it to the human annotator to get annotated. The algorithm then uses the annotated video frame to learn about the environment, retrain the model, and decide which video frame to send in the next round. The key point of active learning is that the algorithm always selects the most important video frame to get annotations, which helps the training process most. Overall, by only selecting a small subset of video frames, active learning is expected to significantly reduce annotation costs.

Our paper [[QSLXLZK, WACV’23]](https://openaccess.thecvf.com/content/WACV2023/html/Qiao_Human-in-the-Loop_Video_Semantic_Segmentation_Auto-Annotation_WACV_2023_paper.html) systematically applies active learning for automatic video semantic segmentation. We propose a novel human-in-the-loop framework, called HVSA ([Human-in-the-Loop Video Semantic Segmentation Auto-Annotation](https://openaccess.thecvf.com/content/WACV2023/html/Qiao_Human-in-the-Loop_Video_Semantic_Segmentation_Auto-Annotation_WACV_2023_paper.html)), to generate semantic segmentation annotations for the entire video using only a small annotation budget. Our method alternates between active learning and training algorithms until annotation quality is satisfied. In particular, the active learning picks the most important samples to get manual annotations, where the sample can be a video frame, a rectangle, or even a super-pixel (ie, a set of pixels with an arbitrary shape). Additionally, the test-time fine-tuning algorithm propagates the manual annotations of selected samples to the entire video. Real-world experiments on the Cityscape dataset show our method generates highly accurate and consistent semantic segmentation annotations while simultaneously enjoying a significantly small(er?) annotation cost.

In the future, building a successful AI self-driving system cannot depend solely on vision information. An interesting research direction is to incorporate more information sources, such as sound and laser.

!

Results on two video frames (Figure 10 of [[QSLXLZK, WACV’23](https://openaccess.thecvf.com/content/WACV2023/html/Qiao_Human-in-the-Loop_Video_Semantic_Segmentation_Auto-Annotation_WACV_2023_paper.html)]). Column (a) is the video frame, (b) costs about 10.4% human annotation clicks with annotating frame, and (c) costs about 44% clicks with annotating frame, (d) is the mimic manual annotation, and (e) is the ground-truth. Our method HVSA achieves similar performance in (b) compared to (c) but costs significantly fewer clicks.

## People

<!-- Table-like structure detected -->

! 

# Chong Liu

Assistant Professor, Department of Computer Science, State University of New York at Albany

Related

Insights

* [BlogMay 30, 2024

  ## Searching for simplicity in microbial communities](https://datascience.uchicago.edu/insights/searching-for-simplicity-in-microbial-communities/)
* [BlogMay 22, 2024

  ## AI as a Great Teacher for Molecular Dynamic Modeling](https://datascience.uchicago.edu/insights/ai-as-a-great-teacher-for-molecular-dynamic-modeling/)
* [BlogJul 29, 2024

  ## Does Political Polarization Really Undermine Democracy? Maybe Not](https://datascience.uchicago.edu/insights/does-political-polarization-really-undermine-democracy-maybe-not/)

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