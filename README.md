# Home Assistant Sungrow Inverter Integration

This integration allows you to monitor and control your Sungrow solar inverter through Home Assistant using Modbus TCP/RTU protocol.

## Features

- Real-time monitoring of solar production
- Battery status monitoring (if applicable)
- Grid connection status
- Power generation statistics
- System status and alarms

## Supported Devices

- Sungrow Inverters with Modbus TCP/RTU support

## Installation

1. Copy the `sungrow_inverter` folder to your Home Assistant's `custom_components` directory
2. Restart Home Assistant
3. Add the integration through the Home Assistant UI

## Configuration

The integration can be configured through the Home Assistant UI:

1. Go to Configuration > Integrations
2. Click on "+ Add Integration"
3. Search for "Sungrow Inverter"
4. Enter the required connection details:
   - Host/IP address (for TCP) or Serial port (for RTU)
   - Port (default: 502 for TCP)
   - Slave ID (default: 1)
   - Connection type (TCP/RTU)

## Modbus Registers

The integration uses the following Modbus registers (based on the official documentation):

- Total power yield (register 5004)
- Total running time (register 5006)
- Internal temperature (register 5008)
- DC voltage and current (registers 5011-5016)
- Grid voltage and current (registers 5019-5024)
- Active power (register 5031)
- Grid frequency (register 5036)
- Work state (register 5038)

## Troubleshooting

If you encounter any issues:

1. Check your network connection to the inverter
2. Verify the Modbus settings in your inverter
3. Check the Home Assistant logs for any error messages
4. Ensure the correct slave ID is configured

## License

This project is licensed under the MIT License - see the LICENSE file for details. 