import matplotlib.pyplot as plt
import numpy as np

import bad_color_map

# Get the list of custom colormaps (excluding reversed versions)
cmap_list = [
    name
    for name in bad_color_map.colormaps.keys()
    if not name.endswith("_r")
]

# Create test image: sine wave superimposed on a ramp function
# The amplitude of the sine wave is progressively reduced to zero at the bottom
x = np.linspace(0, 4 * np.pi, 256)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)

# Ramp function (horizontal gradient from 0 to 1)
ramp = X / (4 * np.pi)

# Sine wave with amplitude that decreases towards the bottom (Y=0)
sine_amplitude = Y  # amplitude varies from 0 at bottom to 1 at top
sine_wave = (
    sine_amplitude * np.sin(X) * 0.5
)  # scale sine to not exceed ramp bounds

# Combine: ramp + sine wave
Z = ramp + sine_wave
Z = np.clip(Z, 0, 1)  # ensure values stay in [0, 1]

# Grid layout: 3 columns
ncols = 3
nrows = int(np.ceil(len(cmap_list) / ncols))

fig, axes = plt.subplots(nrows, ncols, figsize=(12, 3 * nrows))
axes = axes.flatten()

for j, cmap in enumerate(cmap_list):
    ax = axes[j]

    # Plot the sine wave data with the colormap
    im = ax.imshow(
        Z,
        aspect="auto",
        cmap=cmap,
        origin="lower",
        extent=[0, 4 * np.pi, 0, 1],
    )

    ax.set_title(cmap, fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

# Hide any unused subplots
for j in range(len(cmap_list), len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
plt.show()

if True:
    fig.savefig("../figs/sine.png", dpi=600)
