**Problem Statement** - In criminal investigations, eyewitnesses often describe what a suspect looks like, but turning those verbal descriptions into accurate facial sketches depends heavily on skilled artists. The process has following issues:

**Time-consuming** - Manual sketching is a slow, iterative process.
**Subjective** - Sketch descriptions can vary based on the artist’s interpretation.
**Limited Availability** - Skilled forensic artists aren’t always readily available.
**Inherent Bias** - Human bias can influence how features are drawn or interpreted.

**Proposed Solution** - The project proposes an AI-based system that uses powerful image generation models to automatically create facial sketches from text descriptions. By evaluating and comparing the performance of models like Stable Diffusion and Flux, the project aims to identify the best approach which produces the most accurate and consistent sketches for use in criminal investigations. This automated process not only accelerates suspect identification but also reduces subjective interpretation and human error.

**Approach** 

**Dataset** - The FaceCaption dataset contains over 15 million images paired with rich natural language descriptions of facial features. Ideal for training models like Stable Diffusion and Flux, which rely on detailed text to generate accurate images.

Fine-tune - Fine-tuned Stable Diffusion model on FaceCaption Dataset. Leveraged LoRA as strategy to fine tune the model  which is a lightweight fine-tuning method that allows us to adapt large pre-trained models like Stable Diffusion to specific tasks without retraining the entire model.

**Results**

<img width="1098" height="419" alt="results" src="https://github.com/user-attachments/assets/010e6c6d-b2d9-4f2a-ac31-87c97cee3c57" />


**Input Caption** - A man with a rounded face, medium complexion, and prominent goatee. He has thick, slightly arched eyebrows and a broad forehead. His eyes are set beneath a heavy brow ridge, giving him a focused expression. His jawline is soft but full, complemented by full cheeks and a wide nose bridge. His hair is dark, short, and slightly tousled.

**Generated Image**:-

<img width="205" height="206" alt="img1" src="https://github.com/user-attachments/assets/01f77684-4a6d-439e-9004-01ce5e7ddf10" />


**Input Caption** - A disheveled-looking man with unkempt, shaggy hair partially obscuring his forehead and ears. His drooping eyelids and sunken, weary eyes suggest prolonged fatigue or emotional strain. Subtle creases around his eyes and mouth, along with a faint scowl, give him a withdrawn and slightly evasive demeanor, as if he's been wandering unnoticed for days.

**Generated Image**:-

<img width="204" height="204" alt="img2" src="https://github.com/user-attachments/assets/6bb70d29-4248-4776-9e2d-95fb8e1da44c" />
