---
title: "Attention, Please! Revisiting Attentive Probing for Masked Image Modeling"
source: "https://arxiv.org/abs/2506.10178"
author:
  - "[[Bill Psomas]]"
  - "[[Dionysis Christopoulos]]"
  - "[[Eirini Baltzi]]"
  - "[[Ioannis Kakogeorgiou]]"
  - "[[Tilemachos Aravanis]]"
  - "[[Nikos Komodakis]]"
  - "[[Konstantinos Karantzalos]]"
  - "[[Yannis Avrithis]]"
  - "[[Giorgos Tolias]]"
published:
created: 2025-06-15
description: "Abstract page for arXiv paper 2506.10178: Attention, Please! Revisiting Attentive Probing for Masked Image Modeling"
tags:
  - "clippings"
---
\[Submitted on 11 Jun 2025\]

## Title:Attention, Please! Revisiting Attentive Probing for Masked Image Modeling

Authors:, , , , , , , ,

[View PDF](https://arxiv.org/pdf/2506.10178)

> Abstract:As fine-tuning (FT) becomes increasingly impractical at scale, probing is emerging as the preferred evaluation protocol for self-supervised learning (SSL). Yet, the standard linear probing (LP) fails to adequately reflect the potential of models trained with Masked Image Modeling (MIM), due to the distributed nature of patch tokens. This motivates the need for attentive probing, an alternative that uses attention to selectively aggregate patch-level features. Despite its growing adoption, attentive probing remains under-explored, with existing methods suffering from excessive parameterization and poor computational efficiency.  
> In this work, we revisit attentive probing through the lens of the accuracy-efficiency trade-off. We conduct a systematic study of existing methods, analyzing their mechanisms and benchmarking their performance. We introduce efficient probing (EP), a multi-query cross-attention mechanism that eliminates redundant projections, reduces the number of trainable parameters, and achieves up to a 10 $\times$ speed-up over conventional multi-head attention. Despite its simplicity, EP outperforms LP and prior attentive probing approaches across seven benchmarks, generalizes well beyond MIM to diverse pre-training paradigms, produces interpretable attention maps, and achieves strong gains in low-shot and layer-wise settings. Code available at [this https URL](https://github.com/billpsomas/efficient-probing).

| Subjects: | Computer Vision and Pattern Recognition (cs.CV) |
| --- | --- |
| Cite as: | [arXiv:2506.10178](https://arxiv.org/abs/2506.10178) \[cs.CV\] |
|  | (or [arXiv:2506.10178v1](https://arxiv.org/abs/2506.10178v1) \[cs.CV\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2506.10178](https://doi.org/10.48550/arXiv.2506.10178)  arXiv-issued DOI via DataCite (pending registration) |

## Submission history

From: Bill Psomas \[[view email](https://arxiv.org/show-email/ea9bc230/2506.10178)\]  
**\[v1\]** Wed, 11 Jun 2025 21:10:26 UTC (27,717 KB)  

## Bibliographic and Citation Tools

Bibliographic Explorer *([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))*

Connected Papers *([What is Connected Papers?](https://www.connectedpapers.com/about))*

Litmaps *([What is Litmaps?](https://www.litmaps.co/))*

scite Smart Citations *([What are Smart Citations?](https://www.scite.ai/))*

## Code, Data and Media Associated with this Article

alphaXiv *([What is alphaXiv?](https://alphaxiv.org/))*

CatalyzeX Code Finder for Papers *([What is CatalyzeX?](https://www.catalyzex.com/))*

DagsHub *([What is DagsHub?](https://dagshub.com/))*

Gotit.pub *([What is GotitPub?](http://gotit.pub/faq))*

Hugging Face *([What is Huggingface?](https://huggingface.co/huggingface))*

Papers with Code *([What is Papers with Code?](https://paperswithcode.com/))*

ScienceCast *([What is ScienceCast?](https://sciencecast.org/welcome))*

## Demos

Replicate *([What is Replicate?](https://replicate.com/docs/arxiv/about))*

Hugging Face Spaces *([What is Spaces?](https://huggingface.co/docs/hub/spaces))*

TXYZ.AI *([What is TXYZ.AI?](https://txyz.ai/))*

## arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2506.10178) | [Disable MathJax](https://arxiv.org/abs/) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))