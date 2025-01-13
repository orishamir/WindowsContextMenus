import winreg

from src.context_menu import ContextMenu
from src.context_menu_locations import ContextMenuLocation
from src.registry_interaction.registry_location import _RegistryLocation
from src.registry_structs import RegistryKey

RESERVED = 0


def apply_context_menu(
    menu: ContextMenu,
    location: ContextMenuLocation,
) -> str:
    """
    Apply context menu to the registry at `location`.
    """
    built_menu: RegistryKey = menu.build()

    _apply_registry_key(built_menu, _RegistryLocation.from_string(location))

    return f"{location}\\{menu.name}"


def _apply_registry_key(key: RegistryKey, location: _RegistryLocation):
    new_loc = location / key.name

    _create_key(new_loc)

    for value in key.values:
        _set_value(new_loc, value.name, value.type, value.data)

    if not key.subkeys:
        return

    for subkey in key.subkeys:
        _apply_registry_key(subkey, new_loc)


def _create_key(location: _RegistryLocation):
    winreg.CloseKey(winreg.CreateKey(location.top_level, location.subkey))


def _set_value(location: _RegistryLocation, value_name: str, value_type: int, data: str | int):
    with winreg.OpenKey(location.top_level, location.subkey, RESERVED, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, value_name, RESERVED, value_type, data)
