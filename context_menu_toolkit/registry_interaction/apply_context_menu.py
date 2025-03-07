import winreg

from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.context_menu_bindings import ContextMenuBinding
from context_menu_toolkit.registry_structs import RegistryKey
from context_menu_toolkit.registry_structs.registry_path import RegistryPath, TopLevelKey

RESERVED_FLAG = 0

_TOP_LEVEL_KEY_TO_VALUE: dict[TopLevelKey, int] = {
    TopLevelKey.HKEY_CLASSES_ROOT: winreg.HKEY_CLASSES_ROOT,
    TopLevelKey.HKEY_CURRENT_USER: winreg.HKEY_CURRENT_USER,
    TopLevelKey.HKEY_LOCAL_MACHINE: winreg.HKEY_LOCAL_MACHINE,
    TopLevelKey.HKEY_USERS: winreg.HKEY_USERS,
    TopLevelKey.HKEY_CURRENT_CONFIG: winreg.HKEY_CURRENT_CONFIG,
}


def apply_context_menu(
    menu: ContextMenu,
    bindings: list[ContextMenuBinding],
) -> None:
    """Apply context menu to the registry for specified bindings."""
    built_menu: RegistryKey = menu.build()

    for binding in bindings:
        _apply_registry_key(built_menu, binding.construct_registry_path())


def _apply_registry_key(key: RegistryKey, location: RegistryPath) -> None:
    """Apply RegistryKey at `location`."""
    new_loc = location / key.name

    _create_key(new_loc)

    for value in key.values:
        _set_value(new_loc, value.name, value.type, value.data)

    if not key.subkeys:
        return

    for subkey in key.subkeys:
        _apply_registry_key(subkey, new_loc)


def _create_key(location: RegistryPath) -> None:
    winreg.CloseKey(
        winreg.CreateKey(
            _TOP_LEVEL_KEY_TO_VALUE[location.top_level_key],
            location.subkeys,
        ),
    )


def _set_value(location: RegistryPath, value_name: str, value_type: int, data: str | int) -> None:
    with winreg.OpenKey(
        _TOP_LEVEL_KEY_TO_VALUE[location.top_level_key],
        location.subkeys,
        RESERVED_FLAG,
        winreg.KEY_SET_VALUE,
    ) as key:
        winreg.SetValueEx(key, value_name, RESERVED_FLAG, value_type, data)
