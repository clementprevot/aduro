# --------------------------------------------------------------------------------------------------
"""Adds config flow for Aduro."""

from typing import Optional

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession
from homeassistant.helpers.typing import ConfigType

from .api import AduroApiClient
from .const import CONF_ADDRESS, CONF_PIN, CONF_SERIAL, DOMAIN, PLATFORMS

# --------------------------------------------------------------------------------------------------


class AduroFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for aduro."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input: Optional[ConfigType] = None):
        """Handle a flow initialized by the user."""
        self._errors = {}

        if user_input is not None:
            valid = await self._test_credentials(
                user_input[CONF_ADDRESS], user_input[CONF_SERIAL], user_input[CONF_PIN]
            )
            if valid:
                return self.async_create_entry(
                    title=user_input[CONF_SERIAL], data=user_input
                )

            self._errors["base"] = "auth"

        user_input = {}
        # Provide defaults for form
        user_input[CONF_ADDRESS] = ""
        user_input[CONF_SERIAL] = ""
        user_input[CONF_PIN] = ""

        return await self._show_config_form(user_input)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry):
        """Get component options flow."""
        return AduroOptionsFlowHandler(config_entry)

    # pylint: disable=unused-argument
    async def _show_config_form(self, user_input: Optional[ConfigType]):
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_ADDRESS, default=user_input[CONF_ADDRESS]): str,
                    vol.Required(CONF_SERIAL, default=user_input[CONF_SERIAL]): str,
                    vol.Required(CONF_PIN, default=user_input[CONF_PIN]): str,
                }
            ),
            errors=self._errors,
        )

    async def _test_credentials(self, address: str, serial: str, pin: str):
        """Return true if credentials is valid."""
        try:
            session = async_create_clientsession(self.hass)
            client = AduroApiClient(address, serial, pin, session)
            await client.async_get_data()
            return True

        except Exception:  # pylint: disable=broad-except
            pass

        return False


class AduroOptionsFlowHandler(config_entries.OptionsFlow):
    """Config flow options handler for aduro."""

    def __init__(self, config_entry: ConfigEntry):
        """Initialize aduro options flow."""
        self.config_entry = config_entry
        self.options = dict(config_entry.options)

    # pylint: disable=unused-argument
    async def async_step_init(self, user_input: Optional[ConfigType] = None):
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input: Optional[ConfigType] = None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            self.options.update(user_input)
            return await self._update_options()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(x, default=self.options.get(x, True)): bool
                    for x in sorted(PLATFORMS)
                }
            ),
        )

    async def _update_options(self):
        """Update config entry options."""
        return self.async_create_entry(
            title=self.config_entry.data.get(CONF_SERIAL), data=self.options
        )
