# Ultra Calculator

Copyright (C) 2026 Alvar Eklind

This project began in 2023 as an attempt to build my own big calculator containing many different calculators.

## Features

- Basic calculator
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Exponentiation
  - Modulo
- Square root and arbitrary root calculator
- PQ solver
- Pythagoras solver
- Shape calculator
  - 2D shapes
  - 3D shapes
- Kvadreringsregeln
- Konjugatregeln
- Linear equation solver

## Requirements
- Python 3.11 or newer
- InquirerPy

## Installation

Clone the repository:

```bash
git clone https://github.com/Hiphopnej/Ultra-Calculator.git
cd Ultra-Calculator
```

Run the calculator with:

```bash
python -m ultra_calculator.ultra_calculator
```

## Usage

## Running Tests

Unit tests are all located in the `tests/` folder.

Run all unit tests:
```
pytest
```

Run all unit tests and get a detailed coverage report, including missed lines:
```
pytest --cov-report term-missing
```

## Project Structure

```text
Ultra-Calculator/
├── src/
│   └── ultra_calculator/
│       ├── __init__.py
│       ├── calculator.py
│       ├── equation_solver.py
│       ├── konjugatregeln.py
│       ├── kvadreringsregeln.py
│       ├── pq_solver.py
│       ├── pytagoras_solver.py
│       ├── shape_solver.py
│       ├── square_root_calculator.py
│       └── ultra_calculator.py
├── tests/
├── examples/
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## License
Ultra-Calculator is licensed under the GNU General Public License v3.0 (GPL-3.0). See the file `LICENSE` for the full license text.