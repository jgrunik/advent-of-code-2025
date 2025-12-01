# Advent of Code 2025 — Solutions

This repository contains my solutions for [Advent of Code 2025](https://adventofcode.com/2025).  
Each day is in its own folder (for example, `day_01`) and contains the puzzle input, solution scripts, and tests.

## Requirements

- `Python 3.11+` (the repo was developed with Python 3.14 but any modern 3.11+ interpreter should work).
- `pytest` for running tests (dev dependency).

## How to run

Open a terminal in the repository root and run the solver scripts.

Example:

```powershell
# Run day 01 solutions
python day_01/part_1.py
python day_01/part_2.py
```


## Tests

Run the test suite from the repository root:

```powershell
python -m pytest -q
```

The repo includes example-based tests in `day_*/test_*.py` that assert the example answers and a handful of edge cases.
