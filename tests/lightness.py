import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from colorspacious import cspace_converter

import bad_color_map

# Get the list of custom colormaps (excluding reversed versions)
cmap_list = [
    name
    for name in bad_color_map.colormaps.keys()
    if not name.endswith("_r")
]

# Number of colormap samples
x = np.linspace(0.0, 1.0, 256)

# Grid layout: 3 columns
ncols = 3
nrows = int(np.ceil(len(cmap_list) / ncols))

fig, axes = plt.subplots(nrows, ncols, figsize=(12, 3 * nrows))
axes = axes.flatten()

for j, cmap in enumerate(cmap_list):
    ax = axes[j]

    # Get RGB values for colormap and convert to CAM02-UCS colorspace
    # lab[0, :, 0] is the lightness
    rgb = mpl.colormaps[cmap](x)[np.newaxis, :, :3]
    lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)

    # Plot colormap L values
    y_ = lab[0, :, 0]
    c_ = x

    ax.scatter(x, y_, c=c_, cmap=cmap, s=100, linewidths=0.0)

    # Set up the axis limits
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(0.0, 100.0)
    ax.set_title(cmap, fontsize=10)
    ax.set_ylabel("Lightness $L^*$", fontsize=10)
    ax.set_xticklabels([])
    ax.set_xticks([])

# Hide any unused subplots
for j in range(len(cmap_list), len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
plt.show()

if True:
    fig.savefig("../figs/lightness.png", dpi=600)
