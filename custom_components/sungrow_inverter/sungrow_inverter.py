"""Sungrow Inverter integration."""
from __future__ import annotations

import logging
from typing import Any

import requests
from requests.auth import HTTPBasicAuth

from .const import (
    DEFAULT_PORT,
    DEFAULT_TIMEOUT,
    DEFAULT_RETRIES,
    SENSOR_TYPES,
)

_LOGGER = logging.getLogger(__name__)


class SungrowInverter:
    """Sungrow Inverter API client."""

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        port: int = DEFAULT_PORT,
        timeout: int = DEFAULT_TIMEOUT,
        retries: int = DEFAULT_RETRIES,
    ) -> None:
        """Initialize the Sungrow Inverter client."""
        self._host = host
        self._username = username
        self._password = password
        self._port = port
        self._timeout = timeout
        self._retries = retries
        self._session = requests.Session()
        self._session.auth = HTTPBasicAuth(username, password)

    def get_data(self) -> dict[str, Any]:
        """Get data from the Sungrow Inverter."""
        data = {}
        for sensor_type in SENSOR_TYPES:
            try:
                response = self._session.get(
                    f"http://{self._host}:{self._port}/api/v1/{sensor_type}",
                    timeout=self._timeout,
                )
                response.raise_for_status()
                data[sensor_type] = response.json()["value"]
            except requests.exceptions.RequestException as ex:
                _LOGGER.error("Error getting data for %s: %s", sensor_type, ex)
                data[sensor_type] = None

        return data 