"""Sensor platform for Sungrow Inverter integration."""
from __future__ import annotations

from datetime import timedelta
import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_HOST,
    CONF_PASSWORD,
    CONF_USERNAME,
    PERCENTAGE,
    POWER_WATT,
    TEMP_CELSIUS,
    VOLT,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import (
    DEFAULT_PORT,
    DEFAULT_TIMEOUT,
    DEFAULT_RETRIES,
    DOMAIN,
    SENSOR_TYPES,
)
from .sungrow_inverter import SungrowInverter

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=30)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Sungrow Inverter sensors."""
    inverter = SungrowInverter(
        host=config_entry.data[CONF_HOST],
        username=config_entry.data[CONF_USERNAME],
        password=config_entry.data[CONF_PASSWORD],
        port=DEFAULT_PORT,
        timeout=DEFAULT_TIMEOUT,
        retries=DEFAULT_RETRIES,
    )

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="sungrow_inverter",
        update_method=inverter.get_data,
        update_interval=SCAN_INTERVAL,
    )

    await coordinator.async_config_entry_first_refresh()

    entities = []
    for sensor_type in SENSOR_TYPES:
        entities.append(SungrowSensor(coordinator, sensor_type))

    async_add_entities(entities)


class SungrowSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Sungrow Inverter sensor."""

    def __init__(self, coordinator: DataUpdateCoordinator, sensor_type: str) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sensor_type = sensor_type
        self._attr_name = SENSOR_TYPES[sensor_type]["name"]
        self._attr_unique_id = f"sungrow_inverter_{sensor_type}"
        self._attr_device_class = SENSOR_TYPES[sensor_type].get("device_class")
        self._attr_native_unit_of_measurement = SENSOR_TYPES[sensor_type].get("unit")
        self._attr_state_class = SENSOR_TYPES[sensor_type].get("state_class")
        self._attr_icon = SENSOR_TYPES[sensor_type].get("icon")

    @property
    def native_value(self) -> Any:
        """Return the state of the sensor."""
        return self.coordinator.data.get(self._sensor_type) 