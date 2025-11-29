import matplotlib.pyplot as plt
import numpy as np

import bad_color_map

# Get the list of custom colormaps (excluding reversed versions)
cmap_list = [
    name
    for name in bad_color_map.colormaps.keys()
    if not name.endswith("_r")
]

# Create comb/stripe data - alternating vertical bands
x = np.linspace(0, 1, 256)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)

# Create comb pattern - repeating stripes
n_stripes = 20
Z = (np.floor(X * n_stripes) % 2) * Y + (
    1 - np.floor(X * n_stripes) % 2
) * (1 - Y)

# Grid layout: 3 columns
ncols = 3
nrows = int(np.ceil(len(cmap_list) / ncols))

fig, axes = plt.subplots(nrows, ncols, figsize=(12, 3 * nrows))
axes = axes.flatten()

for j, cmap in enumerate(cmap_list):
    ax = axes[j]

    # Plot the comb data with the colormap
    ax.imshow(
        Z,
        aspect="auto",
        cmap=cmap,
        origin="lower",
        extent=[0, 1, 0, 1],
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
    fig.savefig("../figs/comb.png", dpi=600)
