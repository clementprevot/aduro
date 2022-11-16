# --------------------------------------------------------------------------------------------------
"""Sensor platform for Aduro."""

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DEFAULT_NAME, DOMAIN, ICON
from .entity import AduroEntity

# --------------------------------------------------------------------------------------------------


async def async_setup_entry(hass: HomeAssistant, entry, async_add_devices):
    """Set up Aduro sensor based on a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([AduroSensor(coordinator, entry)])


class AduroSensor(AduroEntity, SensorEntity):
    """aduro Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{Platform.SENSOR}"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "aduro__custom_device_class"
