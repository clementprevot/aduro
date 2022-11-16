# --------------------------------------------------------------------------------------------------
"""Constants for Aduro."""

from typing import Final

from homeassistant.const import Platform

# --------------------------------------------------------------------------------------------------

# Base component constants
NAME: Final = "Aduro"
DOMAIN: Final = "aduro"
DOMAIN_DATA: Final = f"{DOMAIN}_data"
VERSION: Final = "0.0.1"
ATTRIBUTION: Final = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL: Final = "https://github.com/clementprevot/aduro/issues"

STARTUP_MESSAGE: Final = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
If you have any issues with this integration, open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

# Icons
ICON: Final = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS: Final = "connectivity"

# Platforms
PLATFORMS: Final = [
    Platform.BINARY_SENSOR,
    Platform.SENSOR,
    Platform.SWITCH,
]

# Configuration and options
CONF_ENABLED: Final = "enabled"
CONF_ADDRESS: Final = "address"
CONF_SERIAL: Final = "serial"
CONF_PIN: Final = "pin"

# Defaults
DEFAULT_NAME: Final = DOMAIN

# Attributes
ATTR_INTEGRATION: Final = "integration"
