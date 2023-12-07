# 🎄 Advent of Python 🎄 

# Your Repository Name

![Tests](https://github.com/Loethor/adventofpython/actions/workflows/tests.yml/badge.svg)

## Overview
This project contains solutions to the [Advent of Code](https://adventofcode.com/) challenges solved in Python

## Structure
The project is structured as follows:

- **`years`**: Contains subfolders with the years.
  - **`<years>`**: Contains the solutions and the tests to the problems of that specific year.
    - **`main.py`**: Entry point to execute individual days or the entire set of days.
    - **`days/`**: Modules for each day's solution.
    - **`data/`**: Contains the input and the example provided for each problem.
    - **`tests/`**: Test modules corresponding to each day's solution.
    - **`utils/`**: Utility functions.

## Installation
1. Clone this repository.
2. Create a virtual environment using `python -m venv venv_name`.
3. Activate the virtual environment:
    - **Windows**: `venv_name\Scripts\activate`
    - **Unix/MacOS**: `source venv_name/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`.

## Usage
- To run a single day's solutions:
`python main.py --day <day_number>`
- To run multiple days' solutions:
`python main.py --day <day_number> <day_number> <day_number>`
- To run all days' solutions:
`python main.py`


## Input
Place input data files for each day in the `data/` directory. The code automatically reads input from these files.

## Advent of Rust
You can also check my Rust implementation of 2022 Advent of code [here](https://github.com/Loethor/adventofcode).

## License
This project is licensed under the [MIT License](LICENSE).
