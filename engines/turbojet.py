from core.engine_cycle import EngineCycle
from typing import Dict

class Turbojet(EngineCycle):
    """
    Turbojet engine model (Eurofighter Typhoon specs).
    Inherits from EngineCycle and adds fuel/combustion/nozzle parameters.
    """
    def __init__(
        self,
        inlet_temp: float,
        inlet_pressure: float,
        pressure_ratio: float,
        gamma: float,
        fuel_to_air_ratio: float = 0.025,
        combustion_efficiency: float = 0.98,
        nozzle_efficiency: float = 0.95,
        cp: float = 1005.0,
        R: float = 287.0
    ) -> None:
        """
        Args:
            inlet_temp (float): Inlet temperature in Kelvin.
            inlet_pressure (float): Inlet pressure in Pascals.
            pressure_ratio (float): Compressor pressure ratio.
            gamma (float): Specific heat ratio.
            fuel_to_air_ratio (float): Fuel-to-air mass ratio (default 0.025 for Eurofighter).
            combustion_efficiency (float): Combustion efficiency (default 0.98).
            nozzle_efficiency (float): Nozzle efficiency (default 0.95).
            cp (float): Specific heat at constant pressure (J/kg·K).
            R (float): Gas constant (J/kg·K).
        """
        super().__init__(inlet_temp, inlet_pressure, pressure_ratio, gamma, cp, R)
        self.fuel_to_air_ratio = fuel_to_air_ratio
        self.combustion_efficiency = combustion_efficiency
        self.nozzle_efficiency = nozzle_efficiency

    def simulate_cycle(self, max_temp: float) -> Dict[str, float]:
        """
        Simulate the full turbojet cycle for the Eurofighter Typhoon.

        Args:
            max_temp (float): Maximum turbine inlet temperature (K).
        Returns:
            Dict[str, float]: Dictionary of key cycle results.
        """
        # Compressor
        T2, P2 = self.exit_temperature_pressure()
        # Combustor (idealized, constant pressure)
        T3 = max_temp
        P3 = P2
        # Turbine (isentropic expansion to slightly above ambient)
        P4 = self.inlet_pressure * 1.2
        T4 = T3 * (P4 / P3) ** ((self.gamma - 1) / self.gamma)
        # Nozzle (expansion to ambient)
        V_exit = (2 * self.gamma * self.R * T4 / (self.gamma - 1) *
                  (1 - (self.inlet_pressure / P4) ** ((self.gamma - 1) / self.gamma))) ** 0.5
        # Performance metrics
        thrust = V_exit * self.nozzle_efficiency
        thermal_eff = self.thermal_efficiency(max_temp) * self.combustion_efficiency
        return {
            "Compressor Exit Temp (K)": T2,
            "Compressor Exit Pressure (Pa)": P2,
            "Turbine Exit Temp (K)": T4,
            "Turbine Exit Pressure (Pa)": P4,
            "Nozzle Exit Velocity (m/s)": V_exit,
            "Specific Thrust (N/kg/s)": thrust,
            "Thermal Efficiency": thermal_eff
        } 