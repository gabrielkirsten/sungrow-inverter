"""Config flow for Sungrow Inverter integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_TYPE
from homeassistant.data_entry_flow import FlowResult
from pymodbus.client import ModbusTcpClient, ModbusSerialClient
from pymodbus.exceptions import ModbusException

from .const import (
    CONF_SLAVE_ID,
    DEFAULT_PORT,
    DEFAULT_SLAVE_ID,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

CONNECTION_TYPES = {
    "tcp": "TCP",
    "rtu": "RTU (Serial)",
}

class SungrowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Sungrow Inverter."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            # Validate connection
            try:
                if user_input[CONF_TYPE] == "tcp":
                    client = ModbusTcpClient(
                        host=user_input[CONF_HOST],
                        port=user_input.get(CONF_PORT, DEFAULT_PORT),
                    )
                else:
                    client = ModbusSerialClient(
                        port=user_input[CONF_HOST],
                        baudrate=9600,
                        bytesize=8,
                        parity="N",
                        stopbits=1,
                    )

                if not client.connect():
                    errors["base"] = "cannot_connect"
                else:
                    client.close()
                    return self.async_create_entry(
                        title=f"Sungrow Inverter ({user_input[CONF_HOST]})",
                        data=user_input,
                    )
            except ModbusException:
                errors["base"] = "cannot_connect"

        data_schema = vol.Schema(
            {
                vol.Required(CONF_TYPE): vol.In(CONNECTION_TYPES),
                vol.Required(CONF_HOST): str,
                vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
                vol.Optional(CONF_SLAVE_ID, default=DEFAULT_SLAVE_ID): int,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        ) 