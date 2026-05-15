# Manga-Morph-Gallery

An interactive GAN-based image synthesis web application that displays AI-generated anime faces in a manga-style infinite gallery. The project uses a trained DCGAN model to generate anime face images and applies latent space interpolation to create smooth morph transitions between two generated characters.

When a user clicks on a manga panel, the selected face opens in a modal where the user can play or manually control the morph animation.

## Dataset

The dataset used is the Anime Face Dataset from Kaggle.

```text
https://www.kaggle.com/datasets/splcher/animefacedataset
```

Dataset folder used:

```text
animefacedataset/images
```

The dataset contains cropped anime face images. These images are resized to `64x64` and normalized before training.

Input data:

```text
Anime face images
```

Output:

```text
Generated anime face images
```

## Algorithms Used

The following image synthesis technique was used:

- DCGAN: Deep Convolutional Generative Adversarial Network
- Latent Space Interpolation

DCGAN contains two main models:

- Generator
- Discriminator

The generator creates fake anime faces from random noise, while the discriminator tries to distinguish real dataset images from generated images.

Latent interpolation is used to create morph transitions between two generated faces.

```python
z = (1 - alpha) * z1 + alpha * z2
```

## Evaluation Metrics

GANs are mainly evaluated visually, but the following training indicators were observed:

- Generator Loss
- Discriminator Loss
- Real Score
- Fake Score
- Visual quality of generated faces
- Diversity of generated faces
- Smoothness of morph transitions

The final model was selected based on the quality of generated samples and smoothness of latent morphing.

## Tech Stack

Machine Learning:

- Python
- PyTorch
- Torchvision
- NumPy

Image Generation:

- DCGAN
- Latent Space Interpolation

Web Framework:

- Flask

Frontend:

- HTML
- CSS
- JavaScript

Development Tools:

- Google Colab
- VS Code
- Git
- GitHub

## Project Structure

```text
Manga-Morph-Gallery/
│
├── src/
│   ├── app.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── style.css
│       │
│       └── morphs/
│           ├── morph_000/
│           │   ├── frame_00.png
│           │   ├── frame_01.png
│           │   └── ...
│           │
│           ├── morph_001/
│           │   ├── frame_00.png
│           │   ├── frame_01.png
│           │   └── ...
│           │
│           └── ...
│
├── assets/
│   └── notebooks/
│       └── GAN.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Start

Train the DCGAN model in Google Colab using the anime face dataset.

After training, save the generator:

```python
torch.save(generator.state_dict(), "G_final.pth")
```

Generate latent morph frames:

```python
z1 = torch.randn(1, latent_size, 1, 1, device=device)
z2 = torch.randn(1, latent_size, 1, 1, device=device)

for step_idx, alpha in enumerate(torch.linspace(0, 1, steps, device=device)):
    z = (1 - alpha) * z1 + alpha * z2

    with torch.no_grad():
        img = generator(z)
```

Save the generated frames inside folders like:

```text
morph_000/frame_00.png
morph_000/frame_01.png
morph_000/frame_02.png
```

Move all morph folders into:

```text
src/static/morphs/
```

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Manga-Morph-Gallery.git
```

Move into the project folder:

```bash
cd Manga-Morph-Gallery
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python src/app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

## Output

The web app displays:

- Manga-style generated anime face gallery
- Infinite scrolling image panels
- AI-generated anime faces
- Clickable image modal
- Latent morph animation
- Slider to move between generated faces
- Play/pause controls for morph transition

## Project Explanation

This project uses a DCGAN to generate anime faces from random latent vectors. Instead of displaying only single generated images, the project explores the model's latent space by interpolating between two random vectors.

Each morph sequence shows how one generated anime face gradually transforms into another. The website presents these generated frames as a manga-style gallery, making the GAN output more interactive and visually engaging.

## Live Demo

```text
Add your deployed website link here
```
```