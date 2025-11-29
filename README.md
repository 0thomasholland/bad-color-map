# Bad colo(u)r map

![PyPI - Version](https://img.shields.io/pypi/v/bad-color-map)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bad-color-map)
![PyPI - License](https://img.shields.io/pypi/l/bad-color-map)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/0thomasholland/bad-color-map/publish.yml?branch=main)
![GitHub Repo Size](https://img.shields.io/github/repo-size/0thomasholland/bad-color-map)
![GitHub last commit](https://img.shields.io/github/last-commit/0thomasholland/bad-color-map)


Some bad color maps for [Matplotlib](https://matplotlib.org/) to make plotting amusing figures easier.

![Painbow Color Map](https://imgs.xkcd.com/comics/painbow_award.png)

## Color maps

![Bad Color Maps](https://raw.githubusercontent.com/0thomasholland/bad-color-map/refs/heads/main/figs/bad_color_maps.png)

![Lightness plots](https://raw.githubusercontent.com/0thomasholland/bad-color-map/refs/heads/main/figs/lightness.png)

Not the most ideal...

## Usage

To use this:

```python
import matplotlib.pyplot as plt
import bad_color_map

plt.XYZ(
    ...
    cmap='painbow'  # or 'michel-levy'
    ...
)

```


![](figs/cielab_grid.png)


## Sources:

- Painbow: [XKCD 2537](https://xkcd.com/2537/)
- Michel-Levy: Bjørn Eske Sørensen; A revised Michel-Lévy interference colour chart based on first-principles calculations. European Journal of Mineralogy 2012;; 25 (1): 5–10. doi: https://doi.org/10.1127/0935-1221/2013/0025-2252
- [Pastel Highlighters](https://www.stabilo.com/uk/highlighter-stabilo-boss-original-pastel/7015-02-5)
- [Original Highlighters](https://www.stabilo.com/uk/highlighter-stabilo-boss-original/7015-01-5)