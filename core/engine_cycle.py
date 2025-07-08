from typing import Tuple
import warnings
try:
    import CoolProp.CoolProp as CP
    _COOLPROP_AVAILABLE = True
except ImportError:
    _COOLPROP_AVAILABLE = False

class EngineCycle:
    """
    Base class for jet engine thermodynamic cycle calculations.
    Supports both ideal and real gas (CoolProp) models.
    """
    def __init__(self, inlet_temp: float, inlet_pressure: float, pressure_ratio: float, gamma: float, cp: float = 1005.0, R: float = 287.0, use_real_gas: bool = False) -> None:
        """
        Initialize the engine cycle.

        Args:
            inlet_temp (float): Inlet temperature in Kelvin.
            inlet_pressure (float): Inlet pressure in Pascals.
            pressure_ratio (float): Compressor pressure ratio (dimensionless).
            gamma (float): Specific heat ratio (Cp/Cv).
            cp (float): Specific heat at constant pressure (J/kg·K). Default is 1005.
            R (float): Gas constant (J/kg·K). Default is 287.
            use_real_gas (bool): If True, use CoolProp for real gas properties.
        """
        self.inlet_temp = inlet_temp
        self.inlet_pressure = inlet_pressure
        self.pressure_ratio = pressure_ratio
        self.gamma = gamma
        self.cp = cp
        self.R = R
        self.use_real_gas = use_real_gas and _COOLPROP_AVAILABLE
        if use_real_gas and not _COOLPROP_AVAILABLE:
            warnings.warn("CoolProp is not installed. Falling back to ideal gas model.")

    def get_cp(self, T: float, P: float) -> float:
        """
        Get specific heat at constant pressure (cp) at given T, P.
        Args:
            T (float): Temperature in K
            P (float): Pressure in Pa
        Returns:
            float: cp in J/kg·K
        """
        if self.use_real_gas:
            return CP.PropsSI('Cpmass', 'T', T, 'P', P, 'Air')
        return self.cp

    def get_enthalpy(self, T: float, P: float) -> float:
        """
        Get specific enthalpy at given T, P.
        Args:
            T (float): Temperature in K
            P (float): Pressure in Pa
        Returns:
            float: Enthalpy in J/kg
        """
        if self.use_real_gas:
            return CP.PropsSI('Hmass', 'T', T, 'P', P, 'Air')
        return self.cp * T

    def exit_temperature_pressure(self) -> Tuple[float, float]:
        """
        Compute the exit temperature and pressure after isentropic compression.
        Returns:
            Tuple[float, float]: (exit temperature in K, exit pressure in Pa)
        """
        T2 = self.inlet_temp * (self.pressure_ratio) ** ((self.gamma - 1) / self.gamma)
        P2 = self.inlet_pressure * self.pressure_ratio
        return T2, P2

    def thermal_efficiency(self, max_temp: float) -> float:
        """
        Compute the ideal Brayton cycle thermal efficiency.
        Args:
            max_temp (float): Maximum cycle temperature (turbine inlet) in K.
        Returns:
            float: Thermal efficiency (dimensionless)
        """
        return 1 - self.inlet_temp / max_temp

    def specific_thrust(self, max_temp: float) -> float:
        """
        Compute the specific thrust (ideal, per unit mass flow).
        Args:
            max_temp (float): Maximum cycle temperature (turbine inlet) in K.
        Returns:
            float: Specific thrust (m/s)
        """
        T2, P2 = self.exit_temperature_pressure()
        T4 = max_temp
        V_exit = (2 * self.gamma * self.R * T4 / (self.gamma - 1) *
                  (1 - (self.inlet_pressure / P2) ** ((self.gamma - 1) / self.gamma))) ** 0.5
        return V_exit 