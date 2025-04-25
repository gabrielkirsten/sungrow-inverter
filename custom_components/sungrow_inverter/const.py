"""Constants for the Sungrow Inverter integration."""
from typing import Final

DOMAIN: Final = "sungrow_inverter"

CONF_HOST: Final = "host"
CONF_USERNAME: Final = "username"
CONF_PASSWORD: Final = "password"

DEFAULT_PORT: Final = 502
DEFAULT_SLAVE_ID: Final = 1
DEFAULT_TIMEOUT: Final = 10
DEFAULT_RETRIES: Final = 3

SENSOR_TYPES: Final = {
    "active_power": {
        "name": "Active Power",
        "unit": "W",
        "icon": "mdi:flash",
    },
    "reactive_power": {
        "name": "Reactive Power",
        "unit": "var",
        "icon": "mdi:flash",
    },
    "apparent_power": {
        "name": "Apparent Power",
        "unit": "VA",
        "icon": "mdi:flash",
    },
    "power_factor": {
        "name": "Power Factor",
        "unit": None,
        "icon": "mdi:flash",
    },
    "grid_voltage": {
        "name": "Grid Voltage",
        "unit": "V",
        "icon": "mdi:flash",
    },
    "grid_current": {
        "name": "Grid Current",
        "unit": "A",
        "icon": "mdi:flash",
    },
    "grid_frequency": {
        "name": "Grid Frequency",
        "unit": "Hz",
        "icon": "mdi:flash",
    },
    "dc_voltage": {
        "name": "DC Voltage",
        "unit": "V",
        "icon": "mdi:flash",
    },
    "dc_current": {
        "name": "DC Current",
        "unit": "A",
        "icon": "mdi:flash",
    },
    "dc_power": {
        "name": "DC Power",
        "unit": "W",
        "icon": "mdi:flash",
    },
    "temperature": {
        "name": "Temperature",
        "unit": "°C",
        "icon": "mdi:thermometer",
    },
    "efficiency": {
        "name": "Efficiency",
        "unit": "%",
        "icon": "mdi:flash",
    },
    "daily_energy": {
        "name": "Daily Energy",
        "unit": "kWh",
        "icon": "mdi:flash",
    },
    "total_energy": {
        "name": "Total Energy",
        "unit": "kWh",
        "icon": "mdi:flash",
    },
} 