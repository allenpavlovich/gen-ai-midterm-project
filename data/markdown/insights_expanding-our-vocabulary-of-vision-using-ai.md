---
title: Expanding Our Vocabulary of Vision Using AI – DSI
original_url: https://datascience.uchicago.edu/insights/expanding-our-vocabulary-of-vision-using-ai
category: insights
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

BlogMay 16, 2024

# Expanding Our Vocabulary of Vision Using AI

Ramanujan Srinath, Eric and Wendy Schmidt AI in Science Postdoctoral Fellow

!

**Figure 1**. AI methods and models have enabled a huge leap in our understanding of how images are processed in the brain. We used to describe visual neurons as “edge detectors” and “face detectors”. Using deep neural networks, we have discovered that images like these (which really can’t be described with words) are richer models of single neurons in our visual system. I liken these AI-enabled descriptions of neural function, perhaps ironically, to a whole new kind of vocabulary that neuroscientists can now use to explain the visual system. (Images from various papers including [a](https://www.nature.com/articles/s41467-021-25409-6), [b](https://www.science.org/doi/10.1126/science.aav9436), [c](https://www.cell.com/cell/fulltext/S0092-8674(19)30391-5?), [d](https://distill.pub/2018/building-blocks/), [e](https://www.biorxiv.org/content/10.1101/2023.11.22.568315v1) , [f](https://pubmed.ncbi.nlm.nih.gov/31686023/))

Our perception of the world is inexorably linked to the words we use to describe it. Our appreciation for and ability to discriminate between different colors or different artistic styles is markedly improved after we acquire the words to describe those colors or artworks. This is called [linguistic](https://en.wikipedia.org/wiki/Linguistic_relativity) [relativity](https://www.youtube.com/watch?v=gMqZR3pqMjg), and while specific examples might be controversial, it certainly has caught the eye of storytellers. In the book *1984*, the authoritarian government introduced ‘Newspeak’ to inhibit people from being able to think critically about policy or oppression. And in *Arrival*, aliens introduce humans to their language to help the humans perceive time differently. In the real world, machine learning and AI methods developed less than a decade ago have introduced a new kind of vocabulary to the neuroscientific understanding of how we see and have had the same kind of revolutionary effect on the field.

Let’s rewind 50 years or so. Neurobiologists had figured out a lot about how neurons work: how they communicate with each other, the anatomy of the eye and various parts of the brain, and the effect of many drugs on the brain and behavior. But questions about how the brain receives inputs from the eye and produces percepts required a fundamental shift in our understanding of the visual system. [Hubel and Wiesel](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2718233/) initiated that shift with their discovery of neurons in the brain that are activated by [elongated bars of light](https://www.youtube.com/watch?v=jw6nBWo21Zk) displayed on a screen. These neurons cared about the orientation of the bar and were dubbed “orientation tuned neurons” because, like you tune an FM radio to a channel frequency, you could tune the activity of the neuron with the orientation and the direction of the moving bar of light. And thus we have our first word — “orientation” — to describe a class of visually sensitive neurons. We can also say that “orientation tuning” is a “word model” of what this neuron does.

!

**Figure 2**. Oliver [Selfridge](https://en.wikipedia.org/wiki/Pandemonium_architecture), an AI pioneer, introduced the pandemonium model of visual pattern recognition in 1959 in which mental “demons” identify simple patterns and lines in the stimuli and shout them out. Cognitive demons listen to these shouts and match it to their more complex patterns. And at the very end, decision demons categorize what is being seen and decide how to interpret or act. This model in various evolved forms was the basis of visual cognitive and neuroscientific thought for decades. (Figure adapted from Lindsay and Norman, 1972)

Since then, neuroscientists have marched faithfully along the hierarchy of visually sensitive areas in the brain to find new kinds of neurons that are activated by different features displayed on the screen. For instance, you can imagine a neuron connected to two orientation tuned neurons to become an “angle” or “corner” neuron. You can put many of them together to form a “curvature” neuron. Instead of edges, you can have neurons sensitive to different “colors” and “textures.” Put all these together to form “object” or “face” or “tool” or “landscape” neurons. You can discover anatomical connections between the hierarchy of visual areas in the brain and come up with theories about how these neurons develop their sensitivities and what would happen if the inputs from the eyes were degraded somehow. If you tell a neuroscientist that a neuron in a specific part of the brain is orientation tuned, they can guess its provenance, development, anatomical connections with its inputs and outputs, the properties of the neurons in its neighborhood, and what would happen if you removed it from the circuit. We have been asking these questions and enriching our understanding of how we visually perceive for decades.

But there has always been a sword of Damocles hanging above our models of vision. Remember the “orientation” tuned neuron? That one was a bit of an exception, turns out\*. As soon as you put two of these simple neurons together, the number of types of responses explode. Indeed, [even Hubel and Wiesel thought](https://journals.physiology.org/doi/pdf/10.1152/jn.1965.28.2.229) it “unwise” to label neurons “curvature” or “corner” detectors because those monikers “neglect the importance of” the other properties of objects. They simply labeled them [“simple”, “complex” or “hypercomplex”](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1890437/) cells and described their responses in great detail while admitting that they were describing a subset of all types and that their descriptions were very likely impoverished. Because of this, none of our models were able to generate good predictions about how neurons would respond to photographs of natural scenes which have an intractably rich variety of visual features. Nevertheless, for fifty years, we have been using all these categorical words to describe the neurons that mediate our perception of the visual world, knowing full well that the categories are imperfect and their boundaries permeable.

\*In fact, even those neurons aren’t exceptions and orientation tuning as a model is probably [just as impoverished](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006897) [a model](https://arxiv.org/abs/1809.10504) as any other.

About a decade ago, visual neuroscientific inquiry was introduced to a new kind of vocabulary, a new kind of model of a neuron. Neuroscientists discovered that deep [convolutional neural networks](https://www.youtube.com/watch?v=KuXjwB4LzSA) that were trained to categorize images (like [AlexNet](https://en.wikipedia.org/wiki/AlexNet)) contained units that could model the responses of visual neurons [better](https://www.pnas.org/doi/10.1073/pnas.1403112111) [than](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003963) [any](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003915) [other](https://www.annualreviews.org/content/journals/10.1146/annurev-vision-082114-035447) model we had. Let’s unpack that.

A machine learning model was trained to bin images into categories like “German Shepard dog” or “table lamp” or “pizza.” It just so happens that the units of computation in that model (individual filters or combinations of filters) respond in similar ways to input images as the units of computation in our brains (individual neurons or combinations of neurons). Scientists could also invert this argument and test the validity of the model by generating images for which the models have specific predictions for neural activity. In other words, they could use the model to create an image that could activate a neuron in the brain more than any other image. So all you need to describe a visual neuron is this image generated by the best model of that neuron — the more like this image a random photograph was, the more the neuron would respond. Now, instead of saying a neuron was “orientation tuned,” you could provide either the deep network model that predicts its activity or an image that maximally drives the neuron.

These findings have moved the needle significantly for many visual neuroscientists. For some, these models are hypothesis generation machines — a good model can predict the responses of neurons in a variety of untested conditions like testing a deep network face neuron model on objects. For others, these models are edifices to be challenged — testing images for which the models have nonsensical predictions about how the brain extracts image information. And for still others, a deep network model of a neuron is a total replacement of the word models that came before it. For most, in the belabored metaphor introduced at the top of this article, these models and images have added a fundamentally new kind of vocabulary to how we describe visual neurons.

This raises deep questions about the goal of the visual neuroscientific enterprise. Are models of neurons that predict their responses to a very large, diverse set of images sufficient to understand visual perception? More fundamentally, what does it mean to “understand” vision? At the limit, if I could create a model that could precisely predict the responses of a visual neuron to every image, have we “understood” vision? Can we declare victory if we have a card catalog of images that maximally drive every single visual neuron in the brain?

Maybe a hint of an answer comes from [Hubel and Wiesel themselves](https://journals.physiology.org/doi/pdf/10.1152/jn.1965.28.2.229) — “… it should perhaps be stressed that a proper understanding of the part played by any cell in a sensory system must depend not simply upon a description of the cell’s responses to sensory stimuli, but also on a knowledge of how the information it conveys is made use of at higher levels… How far such analysis can be carried is anyone’s guess, but it is clear that these transformations … go only a short way toward accounting for the perception of shapes encountered in everyday life.” Also, in the words of perhaps one of the leading philosophers of our time, ChatGPT:

!

**Figure 3**. Example of ChatGPT output.

I take inspiration from that challenge in my work as a Schmidt Sciences AI in Science Postdoctoral Fellow in the Department of Neurobiology. I am interested in how dimensions of visual information are extracted by the brain and then used to make decisions. In a [recent study](https://www.biorxiv.org/content/10.1101/2024.02.14.580134v1), we showed that the reason we can extract information about foreground objects while the background changes dramatically is that the visual information about the foreground and the background is represented orthogonally in the brain. In an upcoming manuscript, we demonstrate that visual neurons guide the extraction of information *and* the behavior based on that information by flexibly modifying their responses based on cognitive demands. We also discovered a possible mechanism by which these visual neurons could be doing that using simulations and AI methods. Stay tuned for an article about those results!

*This work was supported by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Program of Schmidt Science.*

Related

Research

* [Research Initiative

  ## AI + Science](https://datascience.uchicago.edu/research/ai-science/)

Insights

* [BlogMay 30, 2024

  ## Searching for simplicity in microbial communities](https://datascience.uchicago.edu/insights/searching-for-simplicity-in-microbial-communities/)

## More on this topic

[!

BlogFeb 26, 2025

## Federal budget cuts threaten to decimate America’s AI superiority—and other countries are watching](https://datascience.uchicago.edu/insights/federal-budget-cuts-threaten-to-decimate-americas-ai-superiority-and-other-countries-are-watching/)
[![A video frame example from Cityscape dataset where different colors denote different labels in pixel level. For example, red means person and light blue means sky.](https://datascience.uchicago.edu/wp-content/uploads/2024/05/cityscape-750x500.png)

[Image: A video frame example from Cityscape dataset where different colors denote different labels in pixel level. For example, red means person and light blue means sky.]

BlogJun 06, 2024

## Behind Automatic Video Semantic Segmentation](https://datascience.uchicago.edu/insights/behind-automatic-video-semantic-segmentation/)
[![Microbial organisms drive the carbon cycle. Image adapted from Wu et al. 2024 https://doi.org/10.1016/j.scitotenv.2023.168627](https://datascience.uchicago.edu/wp-content/uploads/2024/05/Carbon_cycle-750x500.jpg)

[Image: Microbial organisms drive the carbon cycle. Image adapted from Wu et al. 2024 https://doi.org/10.1016/j.scitotenv.2023.168627]

BlogMay 30, 2024

## Searching for simplicity in microbial communities](https://datascience.uchicago.edu/insights/searching-for-simplicity-in-microbial-communities/)
[![Fig: Formation of HIV capsid simulated by a coarse-grained model.
From: https://www.google.com/url?q=https://www.science.org/doi/epdf/10.1126/sciadv.add7434&sa=D&source=docs&ust=1715014663521469&usg=AOvVaw3fATTBC_yAvxPv6WPYI17_](https://datascience.uchicago.edu/wp-content/uploads/2024/05/HIV-capsid-750x500.png)

[Image: Fig: Formation of HIV capsid simulated by a coarse-grained model.
From: https://www.google.com/url?q=https://www.science.org/doi/epdf/10.1126/sciadv.add7434&sa=D&source=docs&ust=1715014663521469&usg=AOvVaw3fATTBC\_yAvxPv6WPYI17\_]

BlogMay 22, 2024

## AI as a Great Teacher for Molecular Dynamic Modeling](https://datascience.uchicago.edu/insights/ai-as-a-great-teacher-for-molecular-dynamic-modeling/)