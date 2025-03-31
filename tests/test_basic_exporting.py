import itertools
from typing import Literal

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


@pytest.mark.parametrize(
    (
        "display_text",
        "command",
        "icon",
        "shift_click",
        "never_default",
        "no_working_directory",
        "position",
        "separator",
        "note",
        "selection_limit",
        "has_lua_shield",
        "disabled",
    ),
    itertools.product(  # all possible combinations
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
    ),
)
def test_exporting(  # noqa: PLR0913
    display_text: str,
    command: str | None,
    icon: str | None,
    shift_click: bool,
    never_default: bool,
    no_working_directory: bool,
    position: Literal["Top", "Bottom"] | None,
    separator: Literal["After", "Before"] | None,
    note: str | None,
    selection_limit: Literal[1, 15, 100] | None,
    has_lua_shield: bool,
    disabled: bool,
) -> None:
    """Test exporting of ContextMenu, without considering submenus and conditions."""
    menu = ContextMenu(
        display_text=display_text,
        command=command,
        icon=icon,
        shift_click=shift_click,
        disabled=disabled,
        has_lua_shield=has_lua_shield,
        never_default=never_default,
        no_working_directory=no_working_directory,
        note=note,
        position=position,
        selection_limit=selection_limit,
        separator=separator,
        condition=None,
        submenus=[],
    )
    expected_tree = _build_expected_tree(
        display_text=display_text,
        command=command,
        icon=icon,
        shift_click=shift_click,
        never_default=never_default,
        no_working_directory=no_working_directory,
        position=position,
        separator=separator,
        note=note,
        selection_limit=selection_limit,
        has_lua_shield=has_lua_shield,
        disabled=disabled,
    )

    actual = RegistryExporter().export_tree(menu).model_dump()
    expected = expected_tree.model_dump()
    assert actual == expected


def _build_expected_tree(  # noqa: PLR0912, PLR0913
    *,
    display_text: str,
    command: str | None,
    icon: str | None,
    shift_click: bool,
    never_default: bool,
    no_working_directory: bool,
    position: Literal["Top", "Bottom"] | None,
    separator: Literal["After", "Before"] | None,
    note: str | None,
    selection_limit: Literal[1, 15, 100] | None,
    has_lua_shield: bool,
    disabled: bool,
) -> RegistryKey:
    """Build expected RegistryKey tree from menu paramters.

    Warning:
        Order of subkey/value insertion matters!
    """
    tree = RegistryKey(name=display_text)

    tree.add_value(RegistryValue(name="MUIVerb", type=DataType.REG_SZ, data=display_text))

    if command is not None:
        tree.add_subkey(RegistryKey(name="command", values=[RegistryValue(name="", type=DataType.REG_SZ, data=command)]))

    if icon is not None:
        tree.add_value(RegistryValue(name="Icon", type=DataType.REG_SZ, data=icon))

    if shift_click:
        tree.add_value(RegistryValue(name="Extended", type=DataType.REG_SZ, data=""))

    if never_default:
        tree.add_value(RegistryValue(name="NeverDefault", type=DataType.REG_SZ, data=""))

    if no_working_directory:
        tree.add_value(RegistryValue(name="NoWorkingDirectory", type=DataType.REG_SZ, data=""))

    if position is not None:
        tree.add_value(RegistryValue(name="Position", type=DataType.REG_SZ, data=position))

    if separator is not None:
        assert separator in ("Before", "After")

        if separator == "Before":
            tree.add_value(RegistryValue(name="CommandFlags", type=DataType.REG_DWORD, data=0x20))
        elif separator == "After":
            tree.add_value(RegistryValue(name="CommandFlags", type=DataType.REG_DWORD, data=0x40))

    if note is not None:
        tree.add_value(RegistryValue(name="Note", type=DataType.REG_SZ, data=note))

    if selection_limit is not None:
        assert selection_limit in (1, 15, 100)

        if selection_limit == 1:
            tree.add_value(RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data="Single"))
        elif selection_limit == 15:  # noqa: PLR2004
            tree.add_value(RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data="Document"))
        elif selection_limit == 100:  # noqa: PLR2004
            tree.add_value(RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data="Player"))

    if has_lua_shield:
        tree.add_value(RegistryValue(name="HasLUAShield", type=DataType.REG_SZ, data=""))

    if disabled:
        tree.add_value(RegistryValue(name="LegacyDisable", type=DataType.REG_SZ, data=""))
    return tree
