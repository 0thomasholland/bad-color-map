import numpy as np
from PIL import Image

images = [
    "painbow",
    "michel-levy",
    "michel-levy-sRGB",
    "michel-levy-ProPhoto",
    "banana",
    "original-highlighters",
    "pastel-highlighters",
]

for image in images:
    img = Image.open(f"{image}.png")
    pixels = np.array(img)
    colors = pixels[pixels.shape[0] // 2, :, :3] / 255.0
    np.save(f"../src/bad_color_map/{image}.npy", colors)
