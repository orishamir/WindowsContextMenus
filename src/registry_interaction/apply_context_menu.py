from __future__ import annotations

import winreg
from winreg import (
    HKEY_CURRENT_USER,
    HKEY_CLASSES_ROOT,
    HKEY_USERS,
    HKEY_CURRENT_CONFIG,
    HKEY_LOCAL_MACHINE
)

from src.context_menu import ContextMenu
from src.location import Location, RegistryLocation
from src.registry_structs import RegistryKey

TOP_LEVEL_STR_TO_HKEY: dict[str, int] = {
    "HKEY_CLASSES_ROOT": HKEY_CLASSES_ROOT,
    "HKEY_CURRENT_USER": HKEY_CURRENT_USER,
    "HKEY_LOCAL_MACHINE": HKEY_LOCAL_MACHINE,
    "HKEY_USERS": HKEY_USERS,
    "HKEY_CURRENT_CONFIG": HKEY_CURRENT_CONFIG
}

RESERVED = 0


def apply_context_menu(
        menu: ContextMenu,
        locations: list[Location],
) -> list[str]:
    """
    Apply context menu to the registry at `locations`
    """
    built_menu: RegistryKey = menu.build()

    build_in_locations = [f"{loc}\\{menu.name}" for loc in locations]

    locations = map(_location_to_registry_location, locations)
    for location in locations:
        _apply_registry_key(built_menu, location)

    return build_in_locations


def _location_to_registry_location(location: Location) -> RegistryLocation:
    top_level, *subkey = location.split("\\")
    subkey = "\\".join(subkey)

    if top_level not in TOP_LEVEL_STR_TO_HKEY:
        raise ValueError(f'Invalid location top-key "{top_level}"')

    return RegistryLocation(
        TOP_LEVEL_STR_TO_HKEY[top_level],
        subkey
    )


def _apply_registry_key(key: RegistryKey, location: RegistryLocation):
    new_loc = location / key.name

    _create_key(new_loc)

    for value in key.values:
        _set_value(new_loc, value.name, value.type, value.data)

    if not key.subkeys:
        return

    for subkey in key.subkeys:
        _apply_registry_key(subkey, new_loc)


def _create_key(location: RegistryLocation):
    winreg.CloseKey(winreg.CreateKey(location.top_level, location.subkey))


def _set_value(location: RegistryLocation, value_name: str, value_type: int, data: str | int):
    with winreg.OpenKey(location.top_level, location.subkey, RESERVED, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, value_name, RESERVED, value_type, data)
