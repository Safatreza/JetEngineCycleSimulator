def run_demo():
    # Hardcoded Brayton cycle (ideal, no external dependencies)
    cp = 1005
    gamma = 1.4
    R = 287
    T_ambient = 288.15
    P_ambient = 101325
    T_max = 1400
    P_ratio = 10

    def compressor(T1, P1, P2):
        T2 = T1 * (P2 / P1) ** ((gamma - 1) / gamma)
        return T2, P2

    def combustion(T2, P2, T3_desired):
        return T3_desired, P2

    def turbine(T3, P3, P4):
        T4 = T3 * (P4 / P3) ** ((gamma - 1) / gamma)
        return T4, P4

    def nozzle(T4, P4, P_ambient):
        V_exit = (2 * gamma * R * T4 / (gamma - 1) * (1 - (P_ambient / P4) ** ((gamma - 1) / gamma))) ** 0.5
        return V_exit

    # Cycle
    P2 = P_ambient * P_ratio
    T2, P2 = compressor(T_ambient, P_ambient, P2)
    T3, P3 = combustion(T2, P2, T_max)
    P4 = P_ambient * 1.2
    T4, P4 = turbine(T3, P3, P4)
    V_exit = nozzle(T4, P4, P_ambient)
    thrust = V_exit
    thermal_eff = 1 - T_ambient / T_max
    work_output = cp * (T3 - T4 - (T2 - T_ambient))

    print("\n--- Demo Jet Engine Cycle Results (No Dependencies) ---")
    print(f"Thrust (N/kg/s): {thrust:.2f}")
    print(f"Thermal Efficiency: {thermal_eff:.2f}")
    print(f"Net Work Output (J/kg): {work_output:.2f}")

if __name__ == "__main__":
    run_demo() 