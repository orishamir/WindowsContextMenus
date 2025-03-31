import itertools
from typing import Literal, NamedTuple

import pytest

from context_menu_toolkit.models.context_menu import ContextMenu
from context_menu_toolkit.registry.exporting.registry_exporter import RegistryExporter
from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue

DISPLAY_TEXT_OPTIONS = ("My Text",)
COMMAND_OPTIONS = ("cmd.exe /c start chrome.exe",)
ICON_OPTIONS = ("shell32.dll,-30",)
SHIFT_CLICK_OPTIONS = (True, False)
NEVER_DEFAULT_OPTIONS = (True, False)
NO_WORKING_DIRECTORY_OPTIONS = (True, False)
DISABLED_OPTIONS = (True, False)
HAS_LUA_SHIELD_OPTIONS = (True, False)
NOTE_OPTIONS = ("My note",)
POSITION_OPTIONS = (None, "Top", "Bottom")
SELECTION_LIMIT_OPTIONS = (None, 1, 15, 100)
SEPARATOR_OPTIONS = (None, "After", "Before")


class MenuProperties(NamedTuple):
    display_text: str
    command: str | None
    icon: str | None
    shift_click: bool
    never_default: bool
    no_working_directory: bool
    position: Literal["Top", "Bottom"] | None
    separator: Literal["After", "Before"] | None
    note: str | None
    selection_limit: Literal[1, 15, 100] | None
    has_lua_shield: bool
    disabled: bool


@pytest.mark.parametrize(
    ("menu_properties"),
    [
        MenuProperties(*combination)  # type: ignore[arg-type]
        for combination in itertools.product(
            DISPLAY_TEXT_OPTIONS,
            COMMAND_OPTIONS,
            ICON_OPTIONS,
            SHIFT_CLICK_OPTIONS,
            NEVER_DEFAULT_OPTIONS,
            NO_WORKING_DIRECTORY_OPTIONS,
            POSITION_OPTIONS,
            SEPARATOR_OPTIONS,
            NOTE_OPTIONS,
            SELECTION_LIMIT_OPTIONS,
            HAS_LUA_SHIELD_OPTIONS,
            DISABLED_OPTIONS,
        )
    ],
)
def test_exporting(menu_properties: MenuProperties) -> None:
    """Test exporting of ContextMenu, without considering submenus and conditions."""
    menu = ContextMenu(
        display_text=menu_properties.display_text,
        command=menu_properties.command,
        icon=menu_properties.icon,
        shift_click=menu_properties.shift_click,
        disabled=menu_properties.disabled,
        has_lua_shield=menu_properties.has_lua_shield,
        never_default=menu_properties.never_default,
        no_working_directory=menu_properties.no_working_directory,
        note=menu_properties.note,
        position=menu_properties.position,
        selection_limit=menu_properties.selection_limit,
        separator=menu_properties.separator,
        condition=None,
        submenus=[],
    )
    expected_tree = _build_expected_tree(menu_properties)

    actual = RegistryExporter().export_tree(menu).model_dump()
    expected = expected_tree.model_dump()
    assert actual == expected


def _build_expected_tree(menu_properties: MenuProperties) -> RegistryKey:  # noqa: PLR0912
    """Build expected RegistryKey tree from menu paramters.

    Warning:
        Order of subkey/value insertion matters!
    """
    tree = RegistryKey(name=menu_properties.display_text)

    tree.add_value(RegistryValue(name="MUIVerb", type=DataType.REG_SZ, data=menu_properties.display_text))

    if menu_properties.command is not None:
        tree.add_subkey(RegistryKey(name="command", values=[RegistryValue(name="", type=DataType.REG_SZ, data=menu_properties.command)]))

    if menu_properties.icon is not None:
        tree.add_value(RegistryValue(name="Icon", type=DataType.REG_SZ, data=menu_properties.icon))

    if menu_properties.shift_click:
        tree.add_value(RegistryValue(name="Extended", type=DataType.REG_SZ, data=""))

    if menu_properties.never_default:
        tree.add_value(RegistryValue(name="NeverDefault", type=DataType.REG_SZ, data=""))

    if menu_properties.no_working_directory:
        tree.add_value(RegistryValue(name="NoWorkingDirectory", type=DataType.REG_SZ, data=""))

    if menu_properties.position is not None:
        tree.add_value(RegistryValue(name="Position", type=DataType.REG_SZ, data=menu_properties.position))

    if menu_properties.separator is not None:
        assert menu_properties.separator in ("Before", "After")

        if menu_properties.separator == "Before":
            tree.add_value(RegistryValue(name="CommandFlags", type=DataType.REG_DWORD, data=0x20))
        elif menu_properties.separator == "After":
            tree.add_value(RegistryValue(name="CommandFlags", type=DataType.REG_DWORD, data=0x40))

    if menu_properties.note is not None:
        tree.add_value(RegistryValue(name="Note", type=DataType.REG_SZ, data=menu_properties.note))

    if menu_properties.selection_limit is not None:
        assert menu_properties.selection_limit in (1, 15, 100)

        if menu_properties.selection_limit == 1:
            tree.add_value(RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data="Single"))
        elif menu_properties.selection_limit == 15:  # noqa: PLR2004
            tree.add_value(RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data="Document"))
        elif menu_properties.selection_limit == 100:  # noqa: PLR2004
            tree.add_value(RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data="Player"))

    if menu_properties.has_lua_shield:
        tree.add_value(RegistryValue(name="HasLUAShield", type=DataType.REG_SZ, data=""))

    if menu_properties.disabled:
        tree.add_value(RegistryValue(name="LegacyDisable", type=DataType.REG_SZ, data=""))
    return tree
