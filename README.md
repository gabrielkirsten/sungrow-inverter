# Sungrow Inverter Integration for Home Assistant

This integration allows you to monitor your Sungrow inverter through Home Assistant using the Modbus protocol.

## Features

- Real-time monitoring of inverter data
- Support for multiple sensor types including:
  - Active Power (W)
  - Reactive Power (var)
  - Apparent Power (VA)
  - Power Factor
  - Grid Voltage (V)
  - Grid Current (A)
  - Grid Frequency (Hz)
  - DC Voltage (V)
  - DC Current (A)
  - DC Power (W)
  - Temperature (°C)
  - Efficiency (%)
  - Daily Energy (kWh)
  - Total Energy (kWh)
- Easy configuration through the Home Assistant UI

## Installation

1. Copy the contents of this repository to your Home Assistant's `config/custom_components/sungrow_inverter` directory:
   ```bash
   mkdir -p config/custom_components/sungrow_inverter
   cp -r custom_components/sungrow_inverter/* config/custom_components/sungrow_inverter/
   ```
2. Restart Home Assistant.
3. Add the integration through the Home Assistant UI.

## Configuration

The integration can be configured through the Home Assistant UI:

1. Go to **Configuration** > **Integrations**
2. Click on **+ Add Integration**
3. Search for "Sungrow Inverter"
4. Enter the following details:
   - Host/IP address of your inverter
   - Username (if required)
   - Password (if required)
5. Click **Submit**

## Supported Devices

This integration has been tested with the following Sungrow inverter models:
- SH5K-20
- SH3.6K
- SH4.6K
- SH5.0K
- SH6.0K

## Troubleshooting

If you encounter any issues:

1. Check that your inverter is connected to your network
2. Verify that the IP address is correct
3. Ensure your inverter supports Modbus TCP protocol
4. Check the Home Assistant logs for any error messages
5. Verify that the port (default: 8080) is accessible

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 