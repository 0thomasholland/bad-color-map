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

# Horizontal spacing between colormaps
dc = 1.4

fig, ax = plt.subplots(figsize=(9, 4))

locs = []  # locations for text labels

for j, cmap in enumerate(cmap_list):
    # Get RGB values for colormap and convert to CAM02-UCS colorspace
    # lab[0, :, 0] is the lightness
    rgb = mpl.colormaps[cmap](x)[np.newaxis, :, :3]
    lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)

    # Plot colormap L values
    y_ = lab[0, :, 0]
    c_ = x

    ax.scatter(x + j * dc, y_, c=c_, cmap=cmap, s=300, linewidths=0.0)

    # Store locations for colormap labels (center of each colormap)
    locs.append(x[int(x.size / 2.0)] + j * dc)

# Set up the axis limits
ax.set_xlim(-0.1, x[-1] + (len(cmap_list) - 1) * dc + 0.1)
ax.set_ylim(0.0, 100.0)

# Set up labels for colormaps
ax.xaxis.set_ticks_position("top")
ticker = mpl.ticker.FixedLocator(locs)
ax.xaxis.set_major_locator(ticker)
formatter = mpl.ticker.FixedFormatter(cmap_list)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=50)
ax.set_ylabel("Lightness $L^*$", fontsize=12)

plt.tight_layout()
plt.show()

if True:
    fig.savefig("../figs/lightness.png", dpi=600)
