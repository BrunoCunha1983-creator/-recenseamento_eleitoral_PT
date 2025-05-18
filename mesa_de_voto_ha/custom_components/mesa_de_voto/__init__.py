from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform

DOMAIN = "mesa_de_voto"

async def async_setup(hass: HomeAssistant, config: dict):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.async_create_task(
        async_load_platform(hass, "sensor", DOMAIN, {}, entry)
    )
    return True