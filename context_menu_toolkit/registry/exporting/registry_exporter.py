from datetime import datetime

from context_menu_toolkit.context_menu_bindings import ContextMenuBinding
from context_menu_toolkit.models.context_menu import ContextMenu
from context_menu_toolkit.registry.exporting.aqs_conditions_exporter import AqsConditionsExporter
from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes import (
    AppliesTo,
    Command,
    Disabled,
    HasLuaShield,
    Icon,
    MUIVerb,
    NeverDefault,
    Note,
    NoWorkingDirectory,
    Position,
    SelectionModel,
    Separator,
    ShiftClick,
)


class RegistryExporter:
    """Knows how to create a Registrykey from menu."""

    def export_reg_file(self, menu: ContextMenu, bindings: list[ContextMenuBinding]) -> list[str]:
        r"""Export the Context Menu as a .reg file format.

        Example:
            ```
            Windows Registry Editor Version 5.00

            [HKEY_LOCAL_MACHINE\Software\Classes\*\shell\ConvertVideo]
            "MUIVerb"="Convert mp4..."
            ```

        Returns:
            A list of lines of the .reg file.

        References:
            [^1]: <https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23>
        """
        built_menu: RegistryKey = self.export_tree(menu)

        lines = [
            "Windows Registry Editor Version 5.00",
            "",
            "; Created by: ContextMenuToolkit @ https://github.com/orishamir/WindowsContextMenus/",
            f"; Created on: {datetime.now().strftime('%B %d, %Y')}",
            "",
        ]

        for i, binding in enumerate(bindings):
            lines.append(f";;; menu for binding #{i + 1}: access_scope={binding.access_scope}, item_type={binding.explorer_item}")
            lines.extend(
                built_menu.export_reg(
                    binding.to_path(),
                ),
            )
            lines.append(f";;; end of menu for binding #{i + 1}: access_scope={binding.access_scope}, item_type={binding.explorer_item}")

        return lines

    def export_tree(self, menu: ContextMenu) -> RegistryKey:
        """Export as a RegistryKey tree."""
        tree = RegistryKey(name=menu.display_text)

        self._export_attributes(menu, tree)

        if menu.submenus:
            self._export_submenus(menu, tree)

        return tree

    def _export_submenus(self, menu: ContextMenu, tree: RegistryKey) -> None:
        subkeys: list[RegistryKey] = [self.export_tree(submenu) for submenu in menu.submenus]

        tree.add_subkey(
            RegistryKey(name="shell", subkeys=subkeys),
        )

        tree.add_value(
            RegistryValue(name="SubCommands", type=DataType.REG_SZ, data=""),
        )

    def _export_attributes(self, menu: ContextMenu, tree: RegistryKey) -> None:
        MUIVerb(menu.display_text).apply_to_tree(tree)

        if menu.command is not None:
            Command(menu.command).apply_to_tree(tree)

        if menu.icon is not None:
            Icon(menu.icon).apply_to_tree(tree)

        if menu.shift_click:
            ShiftClick().apply_to_tree(tree)

        if menu.never_default:
            NeverDefault().apply_to_tree(tree)

        if menu.no_working_directory:
            NoWorkingDirectory().apply_to_tree(tree)

        if menu.position is not None:
            Position(menu.position).apply_to_tree(tree)

        if menu.separator is not None:
            Separator(menu.separator).apply_to_tree(tree)

        if menu.note is not None:
            Note(menu.note).apply_to_tree(tree)

        if menu.selection_limit is not None:
            SelectionModel(
                "Single"
                if menu.selection_limit == 1
                else "Document"
                if menu.selection_limit == 15  # noqa: PLR2004
                else "Player",
            ).apply_to_tree(tree)

        if menu.has_lua_shield:
            HasLuaShield().apply_to_tree(tree)

        if menu.disabled:
            Disabled().apply_to_tree(tree)

        if menu.condition is not None:
            aqs_condition = AqsConditionsExporter().export_aqs_condition(menu.condition)
            AppliesTo(aqs_condition.to_aqs_string()).apply_to_tree(tree)
