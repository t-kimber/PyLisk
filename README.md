PyLisk: A Python library to interact with the Lisk blockchain.
==============================
<p align="center">
  <img src="docs/_static/pylisk_logo.png" width="100"/>
</p>

[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/t-kimber/pylisk/workflows/CI/badge.svg)](https://github.com/t-kimber/pylisk/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/t-kimber/pylisk/branch/main/graph/badge.svg)](https://codecov.io/gh/t-kimber/pylisk/branch/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python library for interacting with the Lisk blockchain.

### Installation

Prerequisites: Anaconda + Git.

1. Clone the GitHub repository:
```console
git clone https://github.com/t-kimber/pylisk.git
```
2. Change directory:
```console
cd pylisk
```
3. Create the conda environment:
```console
conda env create -n pylisk -f devtools/conda-envs/test_env.yaml
```
4. Activate the environment:
```console
conda activate pylisk
```
5. Install the `pylisk` package:
```console
pip install -e .
```
6. Verify the installation:
```console
pylisk -h
```

### Examples

To _send a transaction_, run the following:

```console
pylisk send -h
```

To _vote for a delegate_, run the following:

```console
pylisk vote -h
```

Pylisk in action

[![Pylisk in action](http://img.youtube.com/vi/BRkzQJrDomI/0.jpg)](https://www.youtube.com/watch?v=BRkzQJrDomI "Pylisk in action")


### Copyright

Copyright (c) 2021, Talia B. Kimber


#### Acknowledgements

Project based on the
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.6.
