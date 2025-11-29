"""bad_color_map - A collection of custom matplotlib colormaps."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

__all__ = []

# Get the directory containing the .npy files
_DATA_DIR = Path(__file__).parent

# Dictionary to store all colormaps
colormaps = {}


def _load_colormaps():
    """Load all .npy files and register them as matplotlib colormaps."""
    for npy_file in _DATA_DIR.glob("*.npy"):
        name = npy_file.stem  # filename without extension

        try:
            # Load the color data
            data = np.load(npy_file)

            # Ensure values are in [0, 1] range
            if data.max() > 1.0:
                data = data / 255.0

            # Create colormap from array of RGB or RGBA values
            cmap = ListedColormap(data, name=name)

            # Register the colormap with matplotlib
            plt.colormaps.register(cmap=cmap, name=name)

            # Also register the reversed version
            plt.colormaps.register(
                cmap=cmap.reversed(),
                name=f"{name}_r",
            )

            # Store in our dictionary
            colormaps[name] = cmap
            colormaps[f"{name}_r"] = cmap.reversed()

            # Add to __all__
            __all__.append(name)

        except Exception as e:
            print(
                f"Warning: Could not load colormap from {npy_file}: {e}",
            )


# Load colormaps when module is imported
_load_colormaps()


def get_cmap(name):
    """Get a colormap by name.

    Parameters
    ----------
    name : str
        Name of the colormap.

    Returns
    -------
    matplotlib.colors.Colormap
        The requested colormap.

    """
    if name in colormaps:
        return colormaps[name]
    return plt.colormaps.get(name)


def list_cmaps():
    """List all available colormaps from this package.

    Returns
    -------
    list
        List of colormap names.

    """
    return [name for name in colormaps if not name.endswith("_r")]
