import matplotlib.pyplot as plt
import numpy as np
from typing import Sequence, Dict

def plot_pareto_front(
    results: Sequence[Dict[str, float]],
    x_metric: str = "Specific Thrust (N/kg/s)",
    y_metric: str = "Thermal Efficiency",
    annotate: bool = False
) -> None:
    """
    Generate a Pareto front plot comparing two metrics (e.g., thrust vs. efficiency).

    Args:
        results: Sequence of dictionaries with performance metrics.
        x_metric: Key for x-axis metric.
        y_metric: Key for y-axis metric.
        annotate: If True, annotate each point with its index.
    """
    x = np.array([r[x_metric] for r in results])
    y = np.array([r[y_metric] for r in results])
    plt.figure(figsize=(7, 5))
    plt.scatter(x, y, c='b', label='Designs')
    # Pareto front (simple sort for monotonic front)
    sorted_idx = np.argsort(x)
    pareto_x = x[sorted_idx]
    pareto_y = y[sorted_idx]
    plt.plot(pareto_x, pareto_y, 'r--', label='Pareto Front')
    if annotate:
        for i, (xi, yi) in enumerate(zip(x, y)):
            plt.annotate(str(i), (xi, yi))
    plt.xlabel(x_metric)
    plt.ylabel(y_metric)
    plt.title(f'Pareto Front: {y_metric} vs. {x_metric}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show() 