"""Sungrow Inverter integration."""
from __future__ import annotations

import logging
from typing import Any

from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException

from .const import (
    DEFAULT_PORT,
    DEFAULT_TIMEOUT,
    DEFAULT_RETRIES,
    SENSOR_TYPES,
)

_LOGGER = logging.getLogger(__name__)


class SungrowInverter:
    """Sungrow Inverter Modbus client."""

    def __init__(
        self,
        host: str,
        port: int = DEFAULT_PORT,
        slave_id: int = 1,
        timeout: int = DEFAULT_TIMEOUT,
        retries: int = DEFAULT_RETRIES,
    ) -> None:
        """Initialize the Sungrow Inverter client."""
        self._host = host
        self._port = port
        self._slave_id = slave_id
        self._timeout = timeout
        self._retries = retries
        self._client = ModbusTcpClient(
            host=host,
            port=port,
            timeout=timeout,
            retries=retries,
        )

    async def connect(self) -> None:
        """Connect to the inverter."""
        if not self._client.connect():
            raise ConnectionError(f"Could not connect to {self._host}:{self._port}")

    async def disconnect(self) -> None:
        """Disconnect from the inverter."""
        self._client.close()

    def get_data(self) -> dict[str, Any]:
        """Get data from the Sungrow Inverter."""
        data = {}
        for sensor_type, sensor_info in SENSOR_TYPES.items():
            try:
                # Read holding registers (function code 0x03)
                # Each register is 16 bits (2 bytes)
                # Most values are 32 bits (2 registers)
                response = self._client.read_holding_registers(
                    address=0x0000,  # Starting address
                    count=2,  # Number of registers to read
                    slave=self._slave_id
                )
                
                if response.isError():
                    raise ModbusException(f"Modbus error: {response}")

                # Convert the response to the appropriate value
                # This is a simplified example - you'll need to map the correct
                # registers and conversion factors for each sensor type
                value = response.registers[0] / 10.0  # Example conversion
                data[sensor_type] = value

            except ModbusException as ex:
                _LOGGER.error("Error getting data for %s: %s", sensor_type, ex)
                data[sensor_type] = None

        return data 