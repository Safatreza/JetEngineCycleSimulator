# Jet Engine Cycle Simulator

A modular, object-oriented Python package for simulating and analyzing jet engine thermodynamic cycles, including real gas effects, afterburning, and altitude/Mach performance.

## File Structure
- `main.py` - Main entry point for the OOP simulation
- `demo_main.py` - Minimal demo version (no dependencies)
- `core/` - Base engine cycle logic
- `engines/` - Engine types (Turbojet, AfterburningTurbojet, etc.)
- `utils/` - Utilities (atmosphere model, constants)
- `visualization/` - Plotting and analysis tools
- `notebooks/` - Example Jupyter notebooks
- `docs/` - Documentation and API docs
- `tests/` - Test cases for utility functions

## Setup Instructions
```bash
# Clone the repo
 git clone <repo-url>
 cd JetEngineCycleSimulator-main
# Install dependencies
 pip install -r requirements.txt
# (Optional) Install CoolProp for real gas effects
 pip install CoolProp
# (Optional) Set up pre-commit hooks
 pre-commit install
```

## How to Run the Main Project
```bash
python main.py
```

## How to Run the Demo Version (No Dependencies)
```bash
python demo_main.py
```

## How to Run Tests
```bash
pytest
```

## How to Run the Streamlit UI
```bash
streamlit run ui/app.py
```

## How to Run Example Notebooks
Open any notebook in the `notebooks/` folder with JupyterLab or VSCode.

## Features
- Modular OOP design (Turbojet, AfterburningTurbojet, etc.)
- Real gas effects via CoolProp
- Altitude & Mach number performance maps
- Trade-off and Pareto analysis
- Cycle diagrams (T-s, P-v)
- DevOps: CI/CD, pre-commit hooks, Docker support

## Usage Example
```python
from engines.turbojet import Turbojet
engine = Turbojet(288.15, 101325, 10, 1.4)
results = engine.simulate_cycle(1400)
print(results)
```

## Visualizations
- Performance maps: `visualization/performance_maps.py`
- Trade-off plots: `visualization/tradeoffs.py`
- Cycle diagrams: `visualization/diagrams.py`

## DevOps Integration
- GitHub Actions: Lint, test, and coverage on push/PR
- Pre-commit: black, flake8, isort
- Docker: `docker-compose up` for local development

## Documentation
- See `USAGE.md` for CLI and script usage
- See `docs/` for API docs and structure overview
- Example notebooks in `notebooks/`
