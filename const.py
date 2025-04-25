"""Constants for the Sungrow Inverter integration."""
from typing import Final

DOMAIN: Final = "sungrow_inverter"

CONF_HOST: Final = "host"
CONF_USERNAME: Final = "username"
CONF_PASSWORD: Final = "password"

DEFAULT_PORT: Final = 8080
DEFAULT_TIMEOUT: Final = 10
DEFAULT_RETRIES: Final = 3

SENSOR_TYPES: Final = [
    "active_power",
    "reactive_power",
    "apparent_power",
    "power_factor",
    "grid_voltage",
    "grid_current",
    "grid_frequency",
    "dc_voltage",
    "dc_current",
    "dc_power",
    "temperature",
    "efficiency",
    "daily_energy",
    "total_energy",
] 