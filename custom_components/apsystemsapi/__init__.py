"""The APsystems API integration."""
# from __future__ import annotations
#
# import asyncio
# from datetime import timedelta
#
# from homeassistant.config_entries import ConfigEntry
# from homeassistant.const import Platform
# from homeassistant.core import HomeAssistant
# from apsystems_api import Api as ApApi
#
#
# from .const import DOMAIN
# from ...helpers.discovery import async_load_platform
# from ...helpers.event import async_track_time_interval
#
# # TODO List the platforms that you want to support.
# # For your initial PR, limit it to 1 platform.
# PLATFORMS: list[Platform] = [Platform.SENSOR]
#
#
# async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
#     """Set up APsystems API from a config entry."""
#
#     hass.data.setdefault(DOMAIN, {})
#     # TODO 1. Create API instance
#     # TODO 2. Validate the API connection (and authentication)
#     # TODO 3. Store an API object for your platforms to access
#     # hass.data[DOMAIN][entry.entry_id] = MyApi(...)
#
#     api = await ApApi.init(username, password)
#     await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
#
#     hass.async_create_task(asyncio.sleep(10))
#
#     hass.data["apsystemsapi"] = api
#
#     async def update_data(now):
#         """Update APSolar data."""
#         # Fetch APSolar data here and update HomeAssistant entities
#         await hass.helpers.dispatcher.async_dispatcher_send(f'{DOMAIN}_update')
#
#     async_track_time_interval(hass, update_data, timedelta(minutes=15))
#
#     hass.async_create_task(
#         async_load_platform(hass, 'sensor', DOMAIN, {})
#     )
#
#
#     return True
#
#
#
# async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
#     """Unload a config entry."""
#     if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
#         hass.data[DOMAIN].pop(entry.entry_id)
#
#     return unload_ok
