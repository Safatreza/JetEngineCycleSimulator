# Usage Guide

## Install Dependencies
```bash
pip install -r requirements.txt
# For real gas effects:
pip install CoolProp
```

## Run a Simulation
```bash
python JetEngineCycleSimulator-main/main.py
```

## Generate Plots (from Python)
```python
from visualization.performance_maps import plot_performance_map
# ... see README.md for example usage
```

## Run Tests
```bash
pytest
pytest --cov=.
```

## Lint and Format
```bash
flake8 .
black .
isort .
```

## Pre-commit Hooks
```bash
pre-commit install
pre-commit run --all-files
```

## Docker
```bash
docker-compose up --build
``` 