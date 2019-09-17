"""
This module contains plotting themes
"""
from typing import Tuple

import matplotlib.pyplot as plt
import matplotlib.font_manager
import seaborn as sns

def poster(fg_color: str = "#404040", accent: str = "#01BCA3") -> Tuple[str]:
    """
    Use my poster figure style.

    To use this style properly, the Roboto font must be installed.

    Parameters
    ----------
    fg_color : str
        The main color used for plots. This is also the second color
        in the palette
    accent : str
        The color used for important data points. This is the first
        color in the color palette

    Returns
    -------
    Tuple[str]
        Colors in the color palette.
    """
    matplotlib.font_manager.findSystemFonts()
    style = {"axes.edgecolor": fg_color,
             "axes.labelcolor": fg_color,
             "text.color": fg_color,
             "xtick.color": fg_color,
             "ytick.color": fg_color,
             "font.family": "sans-serif",
             "font.sans-serif": ["Roboto"]}

    palette = sns.color_palette([accent, fg_color])

    plt.rcParams["legend.frameon"] = False
    sns.set_context("poster", rc={"lines.linewidth": 4})
    sns.set_palette(palette)
    sns.set_style("ticks", style)


def paper() -> Tuple[str]:
    """
    Use my paper figure style.

    Returns
    -------
    Tuple[str]
        Colors in the color palette.
    """
    sns.set_context("paper")
    sns.despine()
    palette = sns.color_palette()

    return palette