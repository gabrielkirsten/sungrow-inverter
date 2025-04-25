"""The Sungrow Inverter integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_USERNAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from .sungrow_inverter import SungrowInverter

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Sungrow Inverter from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    try:
        inverter = SungrowInverter(
            entry.data[CONF_HOST],
            entry.data[CONF_USERNAME],
            entry.data[CONF_PASSWORD],
        )
        await inverter.connect()
    except Exception as ex:
        _LOGGER.error("Error connecting to Sungrow Inverter: %s", ex)
        raise ConfigEntryNotReady from ex

    hass.data[DOMAIN][entry.entry_id] = inverter

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        inverter: SungrowInverter = hass.data[DOMAIN].pop(entry.entry_id)
        await inverter.disconnect()

    return unload_ok 