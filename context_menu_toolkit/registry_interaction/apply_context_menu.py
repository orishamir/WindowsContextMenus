import typing
import winreg

from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.context_menu_bindings import ContextMenuBinding
from context_menu_toolkit.registry_structs import RegistryKey, RegistryValue
from context_menu_toolkit.registry_structs.registry_path import RegistryPath, TopLevelKey

RESERVED_FLAG = 0

_TOP_LEVEL_KEY_TO_VALUE: dict[TopLevelKey, int] = {
    TopLevelKey.HKEY_CLASSES_ROOT: winreg.HKEY_CLASSES_ROOT,  # type: ignore
    TopLevelKey.HKEY_CURRENT_USER: winreg.HKEY_CURRENT_USER,  # type: ignore
    TopLevelKey.HKEY_LOCAL_MACHINE: winreg.HKEY_LOCAL_MACHINE,  # type: ignore
    TopLevelKey.HKEY_USERS: winreg.HKEY_USERS,  # type: ignore
    TopLevelKey.HKEY_CURRENT_CONFIG: winreg.HKEY_CURRENT_CONFIG,  # type: ignore
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
        _set_value(new_loc, value)

    for subkey in key.subkeys:
        _apply_registry_key(subkey, new_loc)


@typing.no_type_check
def _create_key(location: RegistryPath) -> None:
    winreg.CloseKey(
        winreg.CreateKey(
            _TOP_LEVEL_KEY_TO_VALUE[location.top_level_key],
            location.subkeys,
        ),
    )


@typing.no_type_check
def _set_value(location: RegistryPath, value: RegistryValue) -> None:
    with winreg.OpenKey(
        _TOP_LEVEL_KEY_TO_VALUE[location.top_level_key],
        location.subkeys,
        RESERVED_FLAG,
        winreg.KEY_SET_VALUE,
    ) as key:
        winreg.SetValueEx(key, value.name, RESERVED_FLAG, value.type, value.data)
