from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.features import (
    Command,
    Disabled,
    DisplayText,
    HasLuaShield,
    Icon,
    NeverDefault,
    NoWorkingDirectory,
    Position,
    Separator,
    SeperatorLocation,
    ShiftClick,
)
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


class ContextMenuRegistryCompiler:
    """Compiler."""

    def compile(self, menu: ContextMenu) -> RegistryKey:
        """Compile to registry."""
        tree = RegistryKey(name=menu.display_text)

        self._apply_features(menu, tree)

        if menu.submenus:
            subkeys: list[RegistryKey] = [self.compile(submenu) for submenu in menu.submenus]

            tree.add_subkey(
                RegistryKey(name="shell", subkeys=subkeys),
            )

            tree.add_value(
                RegistryValue(name="SubCommands", type=DataType.REG_SZ, data=""),
            )

        return tree

    def _apply_features(self, menu: ContextMenu, tree: RegistryKey) -> None:
        DisplayText(menu.display_text).apply_registry(tree)
        Command(menu.command).apply_registry(tree)

        if menu.icon is not None:
            Icon(menu.icon).apply_registry(tree)

        if menu.shift_click:
            ShiftClick().apply_registry(tree)

        if menu.never_default:
            NeverDefault().apply_registry(tree)

        if menu.no_working_directory is not None:
            NoWorkingDirectory().apply_registry(tree)

        if menu.position is not None:
            Position(menu.position).apply_registry(tree)

        if menu.separator is not None:
            separator_location = SeperatorLocation.After if menu.separator == "After" else SeperatorLocation.Before
            Separator(separator_location).apply_registry(tree)

        if menu.has_lua_shield:
            HasLuaShield().apply_registry(tree)

        if menu.disabled:
            Disabled().apply_registry(tree)
