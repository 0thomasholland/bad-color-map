"""CIELAB colour space visualization of colormaps in a grid layout.

This script plots all colormaps from bad_color_map through CIELAB
(L*a*b*) colour space, showing the path each colormap takes in
separate 3D subplots arranged in a 3-column grid. Each subplot also
displays 4 horizontal slices showing the available colour gamut at
different lightness levels.
"""

import matplotlib.pyplot as plt
import numpy as np
from colorspacious import cspace_convert

import bad_color_map


def create_lab_slice(l_value, resolution=100):
    """Create a coloured slice of CIELAB space at a given L* value.

    Returns the a*, b* coordinates and RGB colours for valid (in-gamut) colours.
    """
    a_range = np.linspace(-100, 100, resolution)
    b_range = np.linspace(-100, 100, resolution)
    a_grid, b_grid = np.meshgrid(a_range, b_range)

    # Create LAB values
    lab_values = np.zeros((resolution, resolution, 3))
    lab_values[:, :, 0] = l_value
    lab_values[:, :, 1] = a_grid
    lab_values[:, :, 2] = b_grid

    # Convert to RGB
    rgb_values = cspace_convert(lab_values, "CIELab", "sRGB1")

    # Find in-gamut colours (RGB values between 0 and 1)
    in_gamut = np.all((rgb_values >= 0) & (rgb_values <= 1), axis=2)

    return a_grid, b_grid, rgb_values, in_gamut


# Get the list of custom colormaps (excluding reversed versions)
cmap_list = [
    name
    for name in bad_color_map.colormaps
    if not name.endswith("_r")
]

# Grid layout: 3 columns
ncols = 3
nrows = int(np.ceil(len(cmap_list) / ncols))

# Create figure with 3D subplots
fig = plt.figure(figsize=(15, 5 * nrows))

# Sample points along each colormap
n_samples = 2560

# L* values for the slices
l_slices = [25, 50, 75, 90]

# Pre-compute the slices (they're the same for all plots)
slice_data = []
for l_val in l_slices:
    a_grid, b_grid, rgb_vals, in_gamut = create_lab_slice(
        l_val,
        resolution=50,
    )
    # Flatten arrays for scatter plotting, keeping only in-gamut points
    a_flat = a_grid[in_gamut]
    b_flat = b_grid[in_gamut]
    rgb_flat = rgb_vals[in_gamut]
    slice_data.append((l_val, a_flat, b_flat, rgb_flat))

for idx, cmap_name in enumerate(cmap_list):
    # Create 3D subplot
    ax = fig.add_subplot(nrows, ncols, idx + 1, projection="3d")

    # Draw the L* slices first (so colormap path appears on top)
    for l_val, a_flat, b_flat, rgb_flat in slice_data:
        # Plot all in-gamut points at once
        l_array = np.full_like(a_flat, l_val)
        ax.scatter(
            a_flat,
            b_flat,
            l_array,
            c=rgb_flat,
            s=2,
            alpha=0.25,
            edgecolors="none",
        )

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

    # Set axis labels
    ax.set_xlabel("a*", fontsize=9)
    ax.set_ylabel("b*", fontsize=9)
    ax.set_zlabel("L*", fontsize=9)

    # Set title
    ax.set_title(cmap_name, fontsize=12, pad=10)

    # Set viewing angle for better visualization
    ax.view_init(elev=20, azim=45)

    # Set consistent axis limits
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_zlim(0, 100)

    # Reduce tick label size
    ax.tick_params(axis="both", which="major", labelsize=7)

plt.suptitle(
    "Colour Map Paths in CIELAB Colour Space",
    fontsize=16,
    y=1.02,
)

plt.tight_layout()
plt.show()

# Save the figure
fig.savefig("../figs/cielab_grid.png", dpi=600, bbox_inches="tight")
