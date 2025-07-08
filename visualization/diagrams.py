import matplotlib.pyplot as plt
import numpy as np
from typing import Sequence

def plot_brayton_cycle_Ts(
    T: Sequence[float],
    s: Sequence[float],
    stage_labels: Sequence[str] = None
) -> None:
    """
    Plot a T-s (Temperature-Entropy) diagram for the Brayton cycle.
    Args:
        T: Sequence of temperatures (K).
        s: Sequence of specific entropies (J/kg·K).
        stage_labels: Optional list of stage names.
    """
    plt.figure(figsize=(7, 5))
    plt.plot(s, T, marker='o')
    if stage_labels:
        for i, label in enumerate(stage_labels):
            plt.annotate(label, (s[i], T[i]))
    plt.xlabel('Entropy (J/kg·K)')
    plt.ylabel('Temperature (K)')
    plt.title('Brayton Cycle T-s Diagram')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_brayton_cycle_Pv(
    P: Sequence[float],
    v: Sequence[float],
    stage_labels: Sequence[str] = None
) -> None:
    """
    Plot a P-v (Pressure-Specific Volume) diagram for the Brayton cycle.
    Args:
        P: Sequence of pressures (Pa).
        v: Sequence of specific volumes (m^3/kg).
        stage_labels: Optional list of stage names.
    """
    plt.figure(figsize=(7, 5))
    plt.plot(v, P, marker='s')
    if stage_labels:
        for i, label in enumerate(stage_labels):
            plt.annotate(label, (v[i], P[i]))
    plt.xlabel('Specific Volume (m³/kg)')
    plt.ylabel('Pressure (Pa)')
    plt.title('Brayton Cycle P-v Diagram')
    plt.grid(True)
    plt.tight_layout()
    plt.show() 