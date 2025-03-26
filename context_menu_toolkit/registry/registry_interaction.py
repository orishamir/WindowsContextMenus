import typing
import winreg

from context_menu_toolkit.registry.registry_structs import RegistryKey, RegistryPath, RegistryValue, TopLevelKey

RESERVED_FLAG = 0

_TOP_LEVEL_KEY_TO_VALUE: dict[TopLevelKey, int] = {
    TopLevelKey.HKEY_CLASSES_ROOT: winreg.HKEY_CLASSES_ROOT,  # type: ignore[attr-defined]
    TopLevelKey.HKEY_CURRENT_USER: winreg.HKEY_CURRENT_USER,  # type: ignore[attr-defined]
    TopLevelKey.HKEY_LOCAL_MACHINE: winreg.HKEY_LOCAL_MACHINE, # type: ignore[attr-defined]
    TopLevelKey.HKEY_USERS: winreg.HKEY_USERS,  # type: ignore[attr-defined]
    TopLevelKey.HKEY_CURRENT_CONFIG: winreg.HKEY_CURRENT_CONFIG,  # type: ignore[attr-defined]
}


def write_registry_key(key: RegistryKey, location: RegistryPath) -> None:
    """Apply RegistryKey at `location`."""
    new_loc = location / key.name

    _create_key(new_loc)

    for value in key.values:
        _set_value(new_loc, value)

    for subkey in key.subkeys:
        write_registry_key(subkey, new_loc)


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
