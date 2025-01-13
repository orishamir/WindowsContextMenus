import json
from typing import Generator

from src.context_menu import ContextMenu
from src.context_menu_locations import ContextMenuLocation
from src.registry_structs import RegistryKey, DataType, RegistryValue


def export_as_reg_file(
    menu: ContextMenu,
    location: ContextMenuLocation,
) -> list[str]:
    built_menu: RegistryKey = menu.build()
    
    return [
        "Windows Registry Editor Version 5.00",
        "",
    ] + list(_build_key(built_menu, location))


def _build_key(registry_key: RegistryKey, location: str) -> Generator[str, None, None]:
    yield f"[{location}\\{registry_key.name}]"
    for value in registry_key.values:
        yield _build_value(value)
    
    yield ""
    for subkey in registry_key.subkeys:
        yield from _build_key(subkey, f"{location}\\{registry_key.name}")


def _build_value(value: RegistryValue) -> str:
    assert value.type in (DataType.REG_SZ, DataType.REG_DWORD)
    
    if value.type is DataType.REG_SZ:
        data_str = json.dumps(value.data)  # escapes "\" and '"'
    elif value.type is DataType.REG_DWORD:
        data_str = f"dword:{value.data}"
    
    if value.name == "":
        return f"@={data_str}"
    return f'"{value.name}"={data_str}'
