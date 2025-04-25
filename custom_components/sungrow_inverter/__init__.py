"""The Sungrow Inverter integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_TYPE
from homeassistant.core import HomeAssistant
from pymodbus.client import ModbusTcpClient, ModbusSerialClient
from pymodbus.exceptions import ModbusException

from .const import (
    CONF_SLAVE_ID,
    DEFAULT_PORT,
    DEFAULT_SLAVE_ID,
    DOMAIN,
    PLATFORMS,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Sungrow Inverter from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    
    # Create Modbus client based on connection type
    if entry.data[CONF_TYPE] == "tcp":
        client = ModbusTcpClient(
            host=entry.data[CONF_HOST],
            port=entry.data.get(CONF_PORT, DEFAULT_PORT),
        )
    else:
        client = ModbusSerialClient(
            port=entry.data[CONF_HOST],
            baudrate=9600,
            bytesize=8,
            parity="N",
            stopbits=1,
        )
    
    # Test connection
    try:
        if not client.connect():
            _LOGGER.error("Failed to connect to Sungrow inverter")
            return False
    except ModbusException as ex:
        _LOGGER.error("Modbus error: %s", ex)
        return False
    
    hass.data[DOMAIN][entry.entry_id] = {
        "client": client,
        "slave_id": entry.data.get(CONF_SLAVE_ID, DEFAULT_SLAVE_ID),
    }
    
    # Set up platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        client = hass.data[DOMAIN][entry.entry_id]["client"]
        client.close()
        hass.data[DOMAIN].pop(entry.entry_id)
    
    return unload_ok 