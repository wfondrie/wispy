# wefpy

This Python package contains Python functions that I've needed to use commonly.
It is broken in to several different modules:

* `wefpy.percolator` contains functions for working with Percolator
  tab-delimited files in Python.
  
* `wefpy.themes` contains functions to set matplotlib/seaborn themes for my
  figures, e.g. for papers and posters.
  
* `wefpy.plot` contains plotting utility functions, such as adding a y=x line to
  a plot.
  
There is currently no separate documentation, but all function are annotated
with clear docstrings. 

## Installation  
As for now (and until I think of a better name), wefpy should be installed
directly from GitHub using pip:

```
pip install git@github.com:wfondrie/wefpy.git
```

The wefpy package requires Python 3.6+.
