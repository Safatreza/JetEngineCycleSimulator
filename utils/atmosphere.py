import math

def isa_temperature(altitude_m: float) -> float:
    """
    Calculate the ISA standard atmosphere temperature at a given altitude.
    Args:
        altitude_m (float): Altitude in meters.
    Returns:
        float: Temperature in Kelvin.
    """
    T0 = 288.15  # Sea level standard temperature (K)
    lapse_rate = -0.0065  # K/m (up to 11 km)
    if altitude_m < 11000:
        return T0 + lapse_rate * altitude_m
    else:
        return 216.65  # Isothermal layer above 11 km

def isa_pressure(altitude_m: float) -> float:
    """
    Calculate the ISA standard atmosphere pressure at a given altitude.
    Args:
        altitude_m (float): Altitude in meters.
    Returns:
        float: Pressure in Pascals.
    """
    P0 = 101325  # Sea level standard pressure (Pa)
    T0 = 288.15  # Sea level standard temperature (K)
    lapse_rate = -0.0065  # K/m
    g0 = 9.80665  # m/s^2
    R = 287.05  # J/kg/K
    if altitude_m < 11000:
        T = isa_temperature(altitude_m)
        return P0 * (T / T0) ** (-g0 / (lapse_rate * R))
    else:
        # Above 11 km, isothermal layer
        P11 = P0 * (216.65 / T0) ** (-g0 / (lapse_rate * R))
        return P11 * math.exp(-g0 * (altitude_m - 11000) / (R * 216.65)) 