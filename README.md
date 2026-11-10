# Ultra Calculator

[![Tests](https://github.com/Hiphopnej/Ultra-Calculator/actions/workflows/tests.yml/badge.svg)](https://github.com/Hiphopnej/Ultra-Calculator/actions/workflows/tests.yml)

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
- Trigonometry calculator
  - Sine
  - Cosine
  - Tangent
  - Arcsine
  - Arccosine
  - Arctangent
  - Supports both radians and degrees
- Logarithms
  - Any float number above 0
  - Any float base
  - Base e

## Requirements
- Python 3.11 or newer
- InquirerPy 0.3.4 or newer (below 0.4)

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
You can import individual calculators and use them independently.
For example, the trigonometry calculator
```python
from ultra_calculator.trigonometry_calculator import trigonometry

result = trigonometry("sin", 90, "degrees")
print(result)
```
This calculates the sin of 90 degrees and prints the result.

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
│       ├── trigonometry_calculator.py
│       ├── logarithm_calculator.py
│       └── main.py
├── tests/
│       ├── test_calculator.py
│       ├── test_squation_solver.py
│       ├── test_konjugatregeln.py
│       ├── test_kvadreringsregeln.py
│       ├── test_pq_solver.py
│       ├── test_pytagoras_solver.py
│       ├── test_shape_solver.py
│       ├── test_square_root.py
│       ├── test_text_functions.py
│       ├── test_trigonometry.py
│       ├── test_logarithm_calculator.py
│       ├── test_ultra_calculator.py
│       └── test_valid_input.py
├── examples/
│       ├── basic_calculator.py
│       ├── equations.py
│       ├── geometry.py
│       ├── konjugatregeln.py
│       ├── kvadreringsregeln.py
│       ├── pq.py
│       ├── pytagoras.py
│       ├── square_root.py
│       ├── trigonometry.py
│       └── logarithms.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## License
Ultra-Calculator is licensed under the GNU General Public License v3.0 (GPL-3.0). See the file `LICENSE` for the full license text.