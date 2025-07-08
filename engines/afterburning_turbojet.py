from engines.turbojet import Turbojet
from typing import Dict

class AfterburningTurbojet(Turbojet):
    """
    Turbojet engine with afterburner (reheat stage).
    Inherits from Turbojet and adds afterburner modeling.
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
        afterburner_efficiency: float = 0.95,
        afterburner_fuel_ratio: float = 0.015,
        cp: float = 1005.0,
        R: float = 287.0,
        use_real_gas: bool = False
    ) -> None:
        """
        Args:
            afterburner_efficiency (float): Afterburner combustion efficiency.
            afterburner_fuel_ratio (float): Additional fuel-to-air ratio for afterburner.
            Other args as in Turbojet.
        """
        super().__init__(inlet_temp, inlet_pressure, pressure_ratio, gamma, fuel_to_air_ratio, combustion_efficiency, nozzle_efficiency, cp, R)
        self.afterburner_efficiency = afterburner_efficiency
        self.afterburner_fuel_ratio = afterburner_fuel_ratio
        self.use_real_gas = use_real_gas

    def simulate_cycle(self, max_temp: float, afterburner_temp: float) -> Dict[str, float]:
        """
        Simulate the full afterburning turbojet cycle.

        Args:
            max_temp (float): Maximum turbine inlet temperature (K).
            afterburner_temp (float): Afterburner exit temperature (K).
        Returns:
            Dict[str, float]: Key cycle results including afterburner effects.
        """
        # Standard turbojet cycle up to turbine exit
        T2, P2 = self.exit_temperature_pressure()
        T3 = max_temp
        P3 = P2
        P4 = self.inlet_pressure * 1.2
        T4 = T3 * (P4 / P3) ** ((self.gamma - 1) / self.gamma)
        # Afterburner (reheat at constant pressure)
        T5 = afterburner_temp
        P5 = self.inlet_pressure  # Assume expansion to ambient
        # Nozzle (expansion to ambient)
        V_exit = (2 * self.gamma * self.R * T5 / (self.gamma - 1) *
                  (1 - (self.inlet_pressure / P5) ** ((self.gamma - 1) / self.gamma))) ** 0.5
        # Additional thrust and fuel
        thrust = V_exit * self.nozzle_efficiency
        additional_fuel = self.afterburner_fuel_ratio * self.afterburner_efficiency
        return {
            "Compressor Exit Temp (K)": T2,
            "Turbine Exit Temp (K)": T4,
            "Afterburner Exit Temp (K)": T5,
            "Nozzle Exit Velocity (m/s)": V_exit,
            "Specific Thrust (N/kg/s)": thrust,
            "Additional Fuel-to-Air Ratio": additional_fuel
        } 