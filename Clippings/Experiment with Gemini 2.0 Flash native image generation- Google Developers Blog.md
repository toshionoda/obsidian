---
title: "Experiment with Gemini 2.0 Flash native image generation- Google Developers Blog"
source: "https://developers.googleblog.com/en/experiment-with-gemini-20-flash-native-image-generation/"
author:
published:
created: 2025-03-26
description: "Developers can now test experimental image output generation with Gemini 2.0 Flash via the Gemini API in Google AI Studio."
tags:
  - "clippings"
---
developers.googleblog.com uses cookies to deliver and enhance the quality of its services and to analyze traffic. If you agree, cookies are also used to serve advertising and to personalize the content and advertisements that you see. [Learn more](https://policies.google.com/technologies/cookies?hl=en).

## Experiment with Gemini 2.0 Flash native image generation

MAR 12, 2025

Product Manager Google AI Studio Product Manager Google DeepMind

In [December](https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/) we first introduced native image output in Gemini 2.0 Flash to trusted testers. Today, we're making it available for developer experimentation across [all regions](https://ai.google.dev/gemini-api/docs/available-regions) currently supported by Google AI Studio. You can test this new capability using an experimental version of Gemini 2.0 Flash ( [gemini-2.0-flash-exp](https://aistudio.google.com/prompts/new_chat?model=gemini-2.0-flash-exp) ) in Google AI Studio and via the Gemini API.

Gemini 2.0 Flash combines multimodal input, enhanced reasoning, and natural language understanding to create images.

Here are some examples of where 2.0 Flash’s multimodal outputs shine:

### 1\. Text and images together

Use Gemini 2.0 Flash to tell a story and it will illustrate it with pictures, keeping the characters and settings consistent throughout. Give it feedback and the model will retell the story or change the style of its drawings.  

<video><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/image-text-gemini-2-image-generation.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>Story and illustration generation in Google AI Studio

### 2\. Conversational image editing

Gemini 2.0 Flash helps you edit images through many turns of a natural language dialogue, great for iterating towards a perfect image, or to explore different ideas together.

<video><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/conversational-image-editing-gemini-2-image-generation_2.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>Multi-turn conversation image editing maintaining context throughout the conversation in Google AI Studio

### 3\. World understanding

Unlike many other image generation models, Gemini 2.0 Flash leverages world knowledge and enhanced reasoning to create the *right* image. This makes it perfect for creating detailed imagery that’s realistic–like illustrating a recipe. While it strives for accuracy, like all language models, its knowledge is broad and general, not absolute or complete.  

<video><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/world-understanding-gemini-2-image-generation_3.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>Interleaved text and image output for a recipe in Google AI Studio

### 4\. Text rendering

Most image generation models struggle to accurately render long sequences of text, often resulting in poorly formatted or illegible characters, or misspellings. Internal benchmarks show that 2.0 Flash has stronger rendering compared to leading competitive models, and great for creating advertisements, social posts, or even invitations.

<video><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/text-rendering-gemini-2-image-generation_2.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>Image outputs with long text rendering in Google AI Studio

## Start making images with Gemini today

Get started with Gemini 2.0 Flash via the Gemini API. Read more about image generation in our [docs](https://ai.google.dev/gemini-api/docs/image-generation).

```
from google import genai
from google.genai import types

client = genai.Client(api_key="GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=(
        "Generate a story about a cute baby turtle in a 3d digital art style. "
        "For each scene, generate an image."
    ),
    config=types.GenerateContentConfig(
        response_modalities=["Text", "Image"]
    ),
)
```

Whether you are building AI agents, developing apps with beautiful visuals like illustrated interactive stories, or brainstorming visual ideas in conversation, Gemini 2.0 Flash allows you to add text and image generation with just a single model. We're eager to see what developers create with native image output and your [feedback](https://discuss.ai.google.dev/c/gemini-api/4) will help us finalize a production-ready version soon.

posted in: Previous Next