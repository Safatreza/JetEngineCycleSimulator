import pytest
from utils.atmosphere import isa_temperature, isa_pressure

def test_isa_temperature_sea_level():
    assert abs(isa_temperature(0) - 288.15) < 1e-2

def test_isa_temperature_11km():
    assert abs(isa_temperature(11000) - 216.65) < 1e-2

def test_isa_pressure_sea_level():
    assert abs(isa_pressure(0) - 101325) < 1

def test_isa_pressure_11km():
    # Standard value at 11km is about 22632 Pa
    assert abs(isa_pressure(11000) - 22632) < 100 