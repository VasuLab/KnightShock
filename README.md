# KnightShock

![CI](https://github.com/VasuLab/RGFROSH/actions/workflows/main.yml/badge.svg?event=push)
[![codecov](https://codecov.io/gh/VasuLab/KnightShock/branch/main/graph/badge.svg?token=K7UP9UPQGS)](https://codecov.io/gh/VasuLab/KnightShock)
[![license](https://img.shields.io/github/license/VasuLab/knightshock.svg)](https://github.com/VasuLab/knightshock/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

> **Warning** 
> 
> KnightShock is currently in alpha; therefore, its interface is not guaranteed to be stable.

KnightShock is a shock tube experiment planning and data analysis Python package developed at Vasu Lab at the
University of Central Florida.

## Installation

> **Note**
> KnightShock requires Python 3.10 or higher.

KnightShock can be cloned with the following command:

```commandline
git clone https://github.com/VasuLab/KnightShock
```

## Contributing

For any bugs or feature requests, create an issue on the 
[issue tracker](https://github.com/VasuLab/KnightShock/issues). 

After cloning the repository, the development environment can be set up with

```
pip install -r requirements.txt
```

Before creating a pull request, be sure to lint

```
black .
```

and run the automated tests

```
pytest
```

These checks will be performed automatically for all pull requests along
with test coverage comparisons.
