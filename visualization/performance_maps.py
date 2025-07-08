import numpy as np
import matplotlib.pyplot as plt
from engines.turbojet import Turbojet
from utils.atmosphere import isa_temperature, isa_pressure
from typing import Callable

def plot_performance_map(
    engine_factory: Callable[..., Turbojet],
    max_temp: float,
    altitudes: np.ndarray,
    mach_numbers: np.ndarray
) -> None:
    """
    Simulate engine performance over a grid of altitudes and Mach numbers.
    Generate contour plots of thrust and efficiency.

    Args:
        engine_factory: Callable that returns a Turbojet instance with given inlet conditions.
        max_temp: Maximum turbine inlet temperature (K).
        altitudes: 1D array of altitudes (m).
        mach_numbers: 1D array of Mach numbers.
    """
    thrust_grid = np.zeros((len(altitudes), len(mach_numbers)))
    eff_grid = np.zeros_like(thrust_grid)
    for i, alt in enumerate(altitudes):
        T_amb = isa_temperature(alt)
        P_amb = isa_pressure(alt)
        for j, mach in enumerate(mach_numbers):
            # Assume inlet velocity = Mach * sqrt(gamma * R * T)
            gamma = 1.4
            R = 287.0
            inlet_velocity = mach * (gamma * R * T_amb) ** 0.5
            engine = engine_factory(T_amb, P_amb, gamma)
            results = engine.simulate_cycle(max_temp)
            thrust_grid[i, j] = results["Specific Thrust (N/kg/s)"]
            eff_grid[i, j] = results["Thermal Efficiency"]
    # Plotting
    X, Y = np.meshgrid(mach_numbers, altitudes)
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    cs1 = axs[0].contourf(X, Y, thrust_grid, cmap="viridis")
    fig.colorbar(cs1, ax=axs[0])
    axs[0].set_title("Specific Thrust (N/kg/s)")
    axs[0].set_xlabel("Mach Number")
    axs[0].set_ylabel("Altitude (m)")
    cs2 = axs[1].contourf(X, Y, eff_grid, cmap="plasma")
    fig.colorbar(cs2, ax=axs[1])
    axs[1].set_title("Thermal Efficiency")
    axs[1].set_xlabel("Mach Number")
    axs[1].set_ylabel("Altitude (m)")
    plt.tight_layout()
    plt.show() 