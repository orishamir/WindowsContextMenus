import typing
import winreg

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryPath, RegistryValue, TopLevelKey

RESERVED_FLAG = 0

_TOP_LEVEL_KEY_TO_VALUE: dict[TopLevelKey, int] = {
    TopLevelKey.HKEY_CLASSES_ROOT: winreg.HKEY_CLASSES_ROOT,
    TopLevelKey.HKEY_CURRENT_USER: winreg.HKEY_CURRENT_USER,
    TopLevelKey.HKEY_LOCAL_MACHINE: winreg.HKEY_LOCAL_MACHINE,
    TopLevelKey.HKEY_USERS: winreg.HKEY_USERS,
    TopLevelKey.HKEY_CURRENT_CONFIG: winreg.HKEY_CURRENT_CONFIG,
}


def write_registry_key(key: RegistryKey, location: RegistryPath) -> None:
    """Apply RegistryKey at `location`."""
    new_loc = location / key.name

    _create_key(new_loc)

    for value in key.values:
        _set_value(new_loc, value)

    for subkey in key.subkeys:
        write_registry_key(subkey, new_loc)


def read_registry_key(location: RegistryPath) -> RegistryKey:
    """Read key at `location`, recursively."""
    with winreg.OpenKey(
        _TOP_LEVEL_KEY_TO_VALUE[location.top_level_key],
        location.subkeys,
        RESERVED_FLAG,
        winreg.KEY_READ,
    ) as key:
        tree = RegistryKey(name=location.parts[-1])
        tree.values.extend(_read_registry_values(key))

        for i in range(1024):
            try:
                subkey_name = winreg.EnumKey(key, i)
                tree.add_subkey(read_registry_key(location / subkey_name))
            except OSError:
                break
    return tree


def _read_registry_values(key: winreg.HKEYType) -> list[RegistryValue]:
    values: list[RegistryValue] = []
    for i in range(1024):
        try:
            name, data, data_type = winreg.EnumValue(key, i)
            values.append(
                RegistryValue(
                    name=name,
                    type=DataType(data_type),
                    data=data,
                ),
            )
        except OSError:
            break
    return values


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
