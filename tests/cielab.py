"""CIELAB colour space visualization of colormaps.

This script plots all colormaps from bad_color_map through CIELAB
(L*a*b*) colour space, showing the path each colormap takes.
"""

import matplotlib.pyplot as plt
import numpy as np
from colorspacious import cspace_convert

import bad_color_map

# Get the list of custom colormaps (excluding reversed versions)
cmap_list = [
    name
    for name in bad_color_map.colormaps
    if not name.endswith("_r")
]

# Create a single large 3D plot
fig = plt.figure(figsize=(14, 12))
ax = fig.add_subplot(111, projection="3d")

# Sample points along each colormap
n_samples = 256

for cmap_name in cmap_list:
    cmap = bad_color_map.get_cmap(cmap_name)

    # Sample the colormap
    t = np.linspace(0, 1, n_samples)
    rgb_colors = cmap(t)[:, :3]  # Get RGB values (exclude alpha)

    # Convert sRGB to CIELAB using colorspacious
    lab_colors = cspace_convert(rgb_colors, "sRGB1", "CIELab")

    lightness = lab_colors[:, 0]  # Lightness (0-100)
    a_star = lab_colors[:, 1]  # Green-Red axis
    b_star = lab_colors[:, 2]  # Blue-Yellow axis

    # Plot the path through CIELAB space
    # Color the line using the colormap itself
    for i in range(len(t) - 1):
        ax.plot(
            a_star[i : i + 2],
            b_star[i : i + 2],
            lightness[i : i + 2],
            color=rgb_colors[i],
            linewidth=3,
            alpha=0.9,
        )

    # Add a single line for legend (use middle color)
    ax.plot(
        [],
        [],
        [],
        color=rgb_colors[len(t) // 2],
        linewidth=3,
        label=cmap_name,
    )

# Set axis labels
ax.set_xlabel("a* (Green ← → Red)", fontsize=12, labelpad=10)
ax.set_ylabel("b* (Blue ← → Yellow)", fontsize=12, labelpad=10)
ax.set_zlabel("L* (Lightness)", fontsize=12, labelpad=10)

# Set title
ax.set_title(
    "Colour Map Paths in CIELAB Colour Space",
    fontsize=16,
    pad=20,
)

# Add legend
ax.legend(loc="upper left", fontsize=10)

# Set viewing angle for better visualization
ax.view_init(elev=20, azim=45)

# Add reference for the axes
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_zlim(0, 100)

plt.tight_layout()
plt.show()

# Save the figure
fig.savefig("../figs/cielab.png", dpi=600, bbox_inches="tight")
