---
title: NeurIPS 2023 Award-winning paper by DSI Faculty Bo Li, DecodingTrust, provides a comprehensive framework for assessing trustworthiness of GPT models – DSI
original_url: https://datascience.uchicago.edu/news/neurips-2023-award-winning-paper-by-dsi-faculty-bo-li-decodingtrust-provides-a-comprehensive-framework-for-assessing-trustworthiness-of-gpt-models
category: news
date: 2025-05-04
---

## Share

* Email page on Facebook (opens new window)
* Share page on X (opens new window)
* Email Page (opens new window)

<!-- Table-like structure detected -->

DSI NewsJan 31, 2024

# NeurIPS 2023 Award-winning paper by DSI Faculty Bo Li, DecodingTrust, provides a comprehensive framework for assessing trustworthiness of GPT models

In a year with a record-breaking number of paper submissions, Bo Li was awarded the NeurIPS Outstanding Paper Award.

From ghostwriting to investment decisions to medical diagnoses, large language models (LLMs) have a wide range of applications. The most popular LLMs, like the multiple iterations of GPT (generative pre-trained transformer), continue to undergo constant updates, but practitioners are hoping to see these models rapidly employed across diverse domains. Despite impressive examples of realistic text production, concerns around privacy, trustworthiness, and other limitations remain. Neubauer Associate Professor of Computer Science and Data Science [Bo Li](https://datascience.uchicago.edu/people/bo-li/)’s DecodingTrust provides the first comprehensive risk assessment platform for LLMs, and reveals some surprising findings about LLMs such as GPT-3.5 and GPT-4.

Li’s award-winning paper, titled “[DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models](https://neurips.cc/virtual/2023/oral/73736),” offers the most comprehensive evaluation of trustworthiness to date. It defines eight trustworthiness perspectives for LLM evaluations, including toxicity, stereotype bias, adversarial robustness, out-of-distribution robustness, robustness on adversarial demonstrations, privacy, machine ethics, and fairness.

!“One major motivation here is to provide a checklist so that people can see all these perspectives to comprehensively understand a model’s ability and trustworthiness,” said Li. Her paper, written in conjunction with co-authors Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi Xiong. Ritik Dutta, Rylan Schaeffer, Sang Truong, Simran Arora, Mantas Mazeika, Dan Hendrycks, Zinan Lin, Yu Cheng, Sanmi Koyejo, and Dawn Song, takes an organized approach to identifying previously unpublished vulnerabilities to trustworthiness threats.

Li and her co-authors reported the performance of GPT-3.5 (colloquially known as ChatGPT) and GPT-4 across all eight measures. Overall, they found that in general, GPT-4 had better performance than GPT-3.5. But these results flipped when using misleading prompts or jailbreaking techniques.

“As we know, GPT-4 has higher instruction following ability. However, if your instructions have a little bit of misleading information or malicious content, the model (GPT-4) will immediately follow it as well,” said Li. “So it’s easier to trick.” The authors hypothesize that GPT-4 is easier to fool because it follows instructions more precisely. This leads GPT-4 to be more vulnerable than GPR-3.5, which isn’t trained with as much precision.

Another surprising finding in the paper is that LLMs understand privacy-related words differently, depending on the phrasing. For example, if a model was told something “in confidence,” it interpreted the phrase differently than “confidentially” and would leak private information in one case but not the other.

Privacy protection also varied with the type of content that was requested. “We find that the model is very unlikely to leak social security numbers, but they leak other information,” explained Li. “That means they indeed, carefully tuned [the model] for security on numbers, so that they are very good. That, on one hand, shows these types of instruction: fine tuning things will help to improve the model alignment analysis. But, on the other hand, it also shows these types of methods are not enough, because we cannot enumerate all the categories or things to protect the model. We need a more systematic approach.”

The third main finding DecodingTrust demonstrated adversarial transferability across different LLMs, including closed and open models, is in general high. No one model outperformed the others across the eight measurements.

“The biggest takeaway is that no model is perfect, and surprisingly, no model dominates on all 8 perspectives. Even though we included GPT-4, which is very capable,” Li said. “But still from some perspectives, it’s not better than other models.”

DecodingTrust represents the most thorough examination into privacy, security, and bias in LLMs to date. It also includes evaluation scenarios and several novel optimization algorithms to generate challenging prompts and data to evaluate different LLMs not originally included in the paper. However, Li’s work on this topic is far from complete.

When asked about future directions, Li responded, “We are working on social harmfulness, particularly in politics, and are in discussion with some other collaborators. We will keep adding more perspectives as well, because this whole thing is still growing. New types of applications will lead to new perspectives, so we’re also maintaining and adding new models and new perspectives.”

[!](http://datascience.uchicago.edu/wp-content/uploads/2024/01/neurips-logo-svg.svg)In the meantime, Li was recognized by The Conference on Neural Information Processing Systems (NeurIPS) for her comprehensive publication. NeurIPS [awarded six papers](https://blog.neurips.cc/2023/12/11/announcing-the-neurips-2023-paper-awards/) across three categories and the 2023 competition was particularly fierce, with a record-setting 13,300 papers submitted. Li’s paper was selected from among those for the Outstanding Benchmark Award.

“Bo and her colleagues have mapped out a rigorous approach for evaluating the trustworthiness of Large Language Models,”  said Michael Franklin, Morton D. Hull Distinguished Service Professor, Senior Advisor to the Provost for Computing and Data Science, and Faculty Co-Director of the Data Science Institute. “This paper represents a necessary step towards enabling LLMs to be put into practice safely.”

Li and her co-authors have made the benchmark [publicly available](https://decodingtrust.github.io/) to help researchers and practitioners better understand the capabilities, limitations, and potential risks involved in deploying these state-of-the-art LLMs. In addition, they created a [leaderboard](https://huggingface.co/spaces/AI-Secure/llm-trustworthy-leaderboard) on Huggingface for researchers and practitioners to track the trustworthiness of different models across the eight measures.

Related

News

* [Campus NewsJan 03, 2024

  ## Eighteen UChicago faculty members receive named, distinguished service professorships in 2024](https://datascience.uchicago.edu/news/eighteen-uchicago-faculty-members-receive-named-distinguished-service-professorships-in-2024/)
* [DSI NewsAug 28, 2023

  ## DSI Continues to Grow with Six New Faculty Joining 2023-24](https://datascience.uchicago.edu/news/dsi-continues-to-grow-with-six-new-faculty-joining-2023-24/)
* [DSI NewsMay 15, 2024

  ## Haifeng Xu won Best Paper Award at leading AI conference for pioneering research on mechanism design for LLMs](https://datascience.uchicago.edu/news/best-paper-at-2024-web-conference-awarded-to-haifeng-xu/)