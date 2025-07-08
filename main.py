# main.py

from engines.turbojet import Turbojet
from engines.afterburning_turbojet import AfterburningTurbojet
from typing import Dict

def create_turbojet() -> Turbojet:
    return Turbojet(288.15, 101325, 10, 1.4)

def create_afterburning_turbojet() -> AfterburningTurbojet:
    return AfterburningTurbojet(288.15, 101325, 10, 1.4)

def run_turbojet_demo() -> Dict[str, float]:
    engine = create_turbojet()
    return engine.simulate_cycle(1400)

def run_afterburning_turbojet_demo() -> Dict[str, float]:
    engine = create_afterburning_turbojet()
    return engine.simulate_cycle(1400, 1800)

def print_results(title: str, results: Dict[str, float]) -> None:
    print(f"\n{title}")
    for k, v in results.items():
        print(f"{k}: {v:.2f}")

def main():
    print_results("Turbojet Example:", run_turbojet_demo())
    print_results("Afterburning Turbojet Example:", run_afterburning_turbojet_demo())

if __name__ == "__main__":
    main()
