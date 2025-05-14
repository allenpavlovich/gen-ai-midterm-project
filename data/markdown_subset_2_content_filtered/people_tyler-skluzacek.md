---
title: Tyler Skluzacek – DSI
original_url: https://datascience.uchicago.edu/people/tyler-skluzacek
category: people
date: 2025-05-04
---

<!-- Table-like structure detected -->

!

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

People

# Tyler Skluzacek

Currently: Research Scientist, Oak Ridge National Lab; Previously: PhD Candidate, University of Chicago

**Bio:**Tyler is a Ph.D. candidate in Computer Science at the University of Chicago, advised by Kyle Chard and Ian Foster. His research interests lie at the intersection of data management, data science, and HPC, focusing on enabling scientists to maximize the utility of massive amounts of data. His work has culminated in the design of the open-source system Xtract that can intelligently formulate metadata extraction workflows for data stored in heterogeneous file formats across leadership-scale computing facilities. Before joining the University of Chicago, he received his B.A. in Applied Mathematics and Statistics from Macalester College.

**Talk Title:**Enabling Data Utility Across the Sciences

**Talk Abstract:** Scientific data repositories are generally chaotic—files spanning heterogeneous domains, studies, and users are stuffed into an increasingly-unsearchable data swamp without regard for organization, discoverability, or usability. Files that could contribute to scientists’ future research may be spread across storage facilities and submerged beneath petabytes of other files, rendering manual annotation and navigation virtually impossible. To remedy this lack of navigability, scientists require a rich search index of metadata, or data about data, extracted from individual files. In this talk, we will explore automated metadata extraction workflows for converting dark data swamps into navigable data collections, given no prior knowledge regarding each file’s schema or provenance. I enable such extraction from files of vastly different structures by building a robust suite of “extractors” that leverage data scientific methods (e.g., keyword analysis, entity recognition, and file type identification) in order to maximize our body of knowledge about a diversity of files.

In this talk, I outline the construction, optimization, and evaluation of Xtract—a scalable metadata extraction system—that automatically constructs extraction plans for files distributed across remote cyberinfrastructure. I illustrate the scale challenges in processing these data, and outline techniques to maximize extraction throughput, by analyzing Xtract’s performance on three real science data sets.