"""Constants for the Sungrow Inverter integration."""
from typing import Final

DOMAIN: Final = "sungrow_inverter"

# Configuration
CONF_SLAVE_ID: Final = "slave_id"
DEFAULT_SLAVE_ID: Final = 1
DEFAULT_PORT: Final = 502

# Platforms
PLATFORMS: Final = ["sensor"]

# Modbus Registers
REGISTER_TOTAL_POWER_YIELD: Final = 5004
REGISTER_TOTAL_RUNNING_TIME: Final = 5006
REGISTER_INTERNAL_TEMPERATURE: Final = 5008
REGISTER_DC_VOLTAGE_1: Final = 5011
REGISTER_DC_CURRENT_1: Final = 5012
REGISTER_DC_VOLTAGE_2: Final = 5013
REGISTER_DC_CURRENT_2: Final = 5014
REGISTER_DC_VOLTAGE_3: Final = 5015
REGISTER_DC_CURRENT_3: Final = 5016
REGISTER_GRID_VOLTAGE_AB: Final = 5019
REGISTER_GRID_VOLTAGE_BC: Final = 5020
REGISTER_GRID_VOLTAGE_CA: Final = 5021
REGISTER_GRID_CURRENT_A: Final = 5022
REGISTER_GRID_CURRENT_B: Final = 5023
REGISTER_GRID_CURRENT_C: Final = 5024
REGISTER_ACTIVE_POWER: Final = 5031
REGISTER_GRID_FREQUENCY: Final = 5036
REGISTER_WORK_STATE: Final = 5038

# Sensor types
SENSOR_TYPES: Final = {
    "total_power_yield": {
        "name": "Total Power Yield",
        "unit": "kWh",
        "icon": "mdi:solar-power",
        "register": REGISTER_TOTAL_POWER_YIELD,
        "scale": 0.1,
    },
    "total_running_time": {
        "name": "Total Running Time",
        "unit": "h",
        "icon": "mdi:clock-outline",
        "register": REGISTER_TOTAL_RUNNING_TIME,
        "scale": 0.1,
    },
    "internal_temperature": {
        "name": "Internal Temperature",
        "unit": "°C",
        "icon": "mdi:thermometer",
        "register": REGISTER_INTERNAL_TEMPERATURE,
        "scale": 0.1,
    },
    "dc_voltage_1": {
        "name": "DC Voltage 1",
        "unit": "V",
        "icon": "mdi:lightning-bolt",
        "register": REGISTER_DC_VOLTAGE_1,
        "scale": 0.1,
    },
    "dc_current_1": {
        "name": "DC Current 1",
        "unit": "A",
        "icon": "mdi:current-dc",
        "register": REGISTER_DC_CURRENT_1,
        "scale": 0.1,
    },
    "grid_voltage_ab": {
        "name": "Grid Voltage AB",
        "unit": "V",
        "icon": "mdi:lightning-bolt",
        "register": REGISTER_GRID_VOLTAGE_AB,
        "scale": 0.1,
    },
    "grid_current_a": {
        "name": "Grid Current A",
        "unit": "A",
        "icon": "mdi:current-ac",
        "register": REGISTER_GRID_CURRENT_A,
        "scale": 0.1,
    },
    "active_power": {
        "name": "Active Power",
        "unit": "W",
        "icon": "mdi:power-plug",
        "register": REGISTER_ACTIVE_POWER,
        "scale": 1,
    },
    "grid_frequency": {
        "name": "Grid Frequency",
        "unit": "Hz",
        "icon": "mdi:sine-wave",
        "register": REGISTER_GRID_FREQUENCY,
        "scale": 0.01,
    },
    "work_state": {
        "name": "Work State",
        "unit": None,
        "icon": "mdi:state-machine",
        "register": REGISTER_WORK_STATE,
        "scale": 1,
    },
} 