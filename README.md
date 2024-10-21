# Urdu OCR

This repository provides resources for generating Urdu words, capturing images, and applying deep learning models for Optical Character Recognition (OCR).

## Project Overview

Key components include:

- **Dataset Creation**: Generating a diverse set of Urdu words and their corresponding images.
- **Model Training**: Applying advanced deep learning architectures to enhance character recognition accuracy.

## Word Generation

- **Purpose**: Generate a comprehensive dataset of Urdu words for training OCR models.
- **Methodology**:
  - Utilizes defined sets of characters (start, middle, end) to create words of varying lengths (1 to 5 characters).
  - Saves generated words and corresponding labels in a CSV format for easy access and processing.

## Image Generation

- **Purpose**: Create visual representations of the generated Urdu words to be used in model training.
- **Methodology**:
  - Formats each generated word in a Microsoft Word document.
  - Captures screenshots of the words to produce images, ensuring a diverse dataset.
  - Images are saved in a structured directory for subsequent processing.


## Fonts used
- Ameer Nastaleeq
- Noto Nastaliq
- Jameel Noori Nastaleeq

## Dataset Size
We created about 700,000 images in total.

## Images Preview

![02_03_25](https://github.com/user-attachments/assets/08661684-7846-4e68-a3eb-a4497cb251e8)

<br>

![02_03_28](https://github.com/user-attachments/assets/f160bf03-020e-4b1c-a98e-bced75b9ab23)


## Deep Learning Models

This project implements the following models for OCR tasks:

- **Hybrid CNN+LSTM**:
  - Combines Convolutional Neural Networks (CNNs) for feature extraction with Long Short-Term Memory (LSTM) networks for sequence prediction.
  - Optimized for recognizing sequential data in character recognition.

- **VGG16**:
  - A deep convolutional neural network known for its simplicity and depth.
  - Utilized for its strong performance in image classification tasks, adapted for Urdu character recognition.

- **Deep CNN**:
  - A custom-designed deep convolutional neural network.
  - Tailored architecture to enhance the recognition of complex Urdu characters.

## Getting Started

To set up the Urdu OCR project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Urdu-OCR.git
   cd Urdu-OCR

2. **Run the models or modify the data generation scripts**