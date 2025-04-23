# main.py

import math
import pandas as pd
import matplotlib.pyplot as plt

# === CONSTANTS ===
cp = 1005        # Specific heat at constant pressure (J/kg·K)
gamma = 1.4      # Heat capacity ratio (Cp/Cv)
R = 287          # Gas constant (J/kg·K)

# Environment and engine inputs
T_ambient = 288.15    # Ambient temperature (K)
P_ambient = 101325    # Ambient pressure (Pa)
T_max = 1400          # Max turbine inlet temp (K)
P_ratio = 10          # Compressor pressure ratio

# === STAGES ===

def compressor(T1, P1, P2):
    """Isentropic compression"""
    T2 = T1 * (P2 / P1) ** ((gamma - 1) / gamma)
    return T2, P2

def combustion(T2, P2, T3_desired):
    """Constant pressure heat addition"""
    return T3_desired, P2

def turbine(T3, P3, P4):
    """Isentropic expansion"""
    T4 = T3 * (P4 / P3) ** ((gamma - 1) / gamma)
    return T4, P4

def nozzle(T4, P4, P_ambient):
    """Expansion to ambient (isentropic)"""
    V_exit = (2 * gamma * R * T4 / (gamma - 1) *
              (1 - (P_ambient / P4) ** ((gamma - 1) / gamma))) ** 0.5
    return V_exit

# === CYCLE SIMULATION ===

def run_cycle():
    states = {}

    # Ambient
    states['Ambient'] = {'T': T_ambient, 'P': P_ambient}

    # Compressor
    P2 = P_ambient * P_ratio
    T2, P2 = compressor(T_ambient, P_ambient, P2)
    states['Compressor Exit'] = {'T': T2, 'P': P2}

    # Combustion
    T3, P3 = combustion(T2, P2, T_max)
    states['Combustor Exit'] = {'T': T3, 'P': P3}

    # Turbine
    P4 = P_ambient * 1.2  # Assumed slightly above ambient
    T4, P4 = turbine(T3, P3, P4)
    states['Turbine Exit'] = {'T': T4, 'P': P4}

    # Nozzle
    V_exit = nozzle(T4, P4, P_ambient)
    states['Nozzle Exit'] = {'T': T4, 'P': P_ambient, 'V_exit': V_exit}

    # Performance metrics
    thrust = V_exit  # N per kg/s
    thermal_eff = 1 - T_ambient / T_max
    work_output = cp * (T3 - T4 - (T2 - T_ambient))

    return states, {
        'Thrust (N/kg/s)': thrust,
        'Thermal Efficiency': thermal_eff,
        'Net Work Output (J/kg)': work_output
    }

# === DISPLAY ===

def print_results(states, results):
    df = pd.DataFrame(states).T[['T', 'P']]
    df.columns = ['Temperature (K)', 'Pressure (Pa)']
    print("\n--- Jet Engine Cycle States ---")
    print(df.round(2))

    print("\n--- Performance Metrics ---")
    for k, v in results.items():
        print(f"{k}: {v:.2f}")

    # Plotting
    stages = df.index.tolist()
    T = df['Temperature (K)']
    P = df['Pressure (Pa)'] / 1000

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.plot(stages, T, 'r-o', label='Temperature')
    ax2.plot(stages, P, 'b-s', label='Pressure')

    ax1.set_xlabel('Stage')
    ax1.set_ylabel('Temperature (K)', color='r')
    ax2.set_ylabel('Pressure (kPa)', color='b')
    plt.title('Brayton Cycle - Jet Engine Simulator')
    fig.tight_layout()
    plt.show()

# === MAIN ===

if __name__ == "__main__":
    states, results = run_cycle()
    print_results(states, results)
