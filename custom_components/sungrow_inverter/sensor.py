"""Sensor platform for Sungrow Inverter integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    ELECTRIC_CURRENT_AMPERE,
    ELECTRIC_POTENTIAL_VOLT,
    ENERGY_KILO_WATT_HOUR,
    FREQUENCY_HERTZ,
    POWER_WATT,
    TEMP_CELSIUS,
    TIME_HOURS,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse

from .const import DOMAIN, SENSOR_TYPES

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Sungrow Inverter sensors."""
    inverter_data = hass.data[DOMAIN][entry.entry_id]
    client = inverter_data["client"]
    slave_id = inverter_data["slave_id"]

    entities = []
    for sensor_type in SENSOR_TYPES:
        entities.append(
            SungrowSensor(
                client,
                slave_id,
                sensor_type,
                SENSOR_TYPES[sensor_type],
            )
        )

    async_add_entities(entities, True)

class SungrowSensor(SensorEntity):
    """Representation of a Sungrow Inverter sensor."""

    def __init__(
        self,
        client,
        slave_id: int,
        sensor_type: str,
        sensor_info: dict[str, Any],
    ) -> None:
        """Initialize the sensor."""
        self._client = client
        self._slave_id = slave_id
        self._sensor_type = sensor_type
        self._name = sensor_info["name"]
        self._unit = sensor_info["unit"]
        self._icon = sensor_info["icon"]
        self._register = sensor_info["register"]
        self._scale = sensor_info["scale"]
        self._value = None

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return f"sungrow_{self._sensor_type}"

    @property
    def native_value(self) -> float | None:
        """Return the state of the sensor."""
        return self._value

    @property
    def native_unit_of_measurement(self) -> str | None:
        """Return the unit of measurement."""
        return self._unit

    @property
    def icon(self) -> str | None:
        """Return the icon to use in the frontend."""
        return self._icon

    @property
    def device_class(self) -> SensorDeviceClass | None:
        """Return the device class of the sensor."""
        if self._unit == ENERGY_KILO_WATT_HOUR:
            return SensorDeviceClass.ENERGY
        if self._unit == POWER_WATT:
            return SensorDeviceClass.POWER
        if self._unit == ELECTRIC_POTENTIAL_VOLT:
            return SensorDeviceClass.VOLTAGE
        if self._unit == ELECTRIC_CURRENT_AMPERE:
            return SensorDeviceClass.CURRENT
        if self._unit == FREQUENCY_HERTZ:
            return SensorDeviceClass.FREQUENCY
        if self._unit == TEMP_CELSIUS:
            return SensorDeviceClass.TEMPERATURE
        if self._unit == TIME_HOURS:
            return SensorDeviceClass.DURATION
        return None

    @property
    def state_class(self) -> SensorStateClass | None:
        """Return the state class of the sensor."""
        if self._sensor_type in ["total_power_yield", "total_running_time"]:
            return SensorStateClass.TOTAL
        return SensorStateClass.MEASUREMENT

    async def async_update(self) -> None:
        """Get the latest data from the inverter."""
        try:
            result = await self.hass.async_add_executor_job(
                self._client.read_holding_registers,
                self._register,
                1,
                self._slave_id,
            )
        except ModbusException as ex:
            _LOGGER.error("Modbus error: %s", ex)
            return

        if isinstance(result, ExceptionResponse):
            _LOGGER.error("Modbus exception: %s", result)
            return

        if not result.isError():
            self._value = result.registers[0] * self._scale
        else:
            _LOGGER.error("Modbus error: %s", result) 