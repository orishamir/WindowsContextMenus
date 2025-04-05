from context_menu_toolkit.models.conditions import Condition
from context_menu_toolkit.models.context_menu import ContextMenu
from context_menu_toolkit.registry.registry_structs import RegistryKey
from context_menu_toolkit.registry.shell_attributes import (
    AppliesTo,
    Command,
    Disabled,
    EntryName,
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


class RegistryImporter:
    """Import a ContextMenu from Registrykey."""

    def import_menu(self, tree: RegistryKey) -> ContextMenu:
        """Import menu from a RegistryKey tree."""
        menu = ContextMenu(display_text=tree.name)

        self._import_attributes(tree, menu)
        self._import_subkeys(tree, menu)

        return menu

    def _import_subkeys(self, root: RegistryKey, menu: ContextMenu) -> None:
        if len(root.subkeys) != 1:
            return

        shell_subkey = root.subkeys[0]
        if shell_subkey.name.lower() != "shell":
            return

        menu.submenus = [self.import_menu(subtree) for subtree in shell_subkey.subkeys]

    def _import_attributes(self, tree: RegistryKey, menu: ContextMenu) -> None:  # noqa: PLR0912
        command = Command.from_tree(tree)
        icon = Icon.from_tree(tree)
        shift_click = ShiftClick.from_tree(tree)
        never_default = NeverDefault.from_tree(tree)
        no_working_directory = NoWorkingDirectory.from_tree(tree)
        position = Position.from_tree(tree)
        separator = Separator.from_tree(tree)
        note = Note.from_tree(tree)
        has_lua_shield = HasLuaShield.from_tree(tree)
        disabled = Disabled.from_tree(tree)
        display_text = MUIVerb.from_tree(tree)
        selection_limit = SelectionModel.from_tree(tree)
        applies_to = AppliesTo.from_tree(tree)
        display_text = MUIVerb.from_tree(tree)
        fallback_display_text = EntryName.from_tree(tree)

        if icon is not None:
            menu.icon = icon.icon_path

        if display_text is not None:
            menu.display_text = display_text.text

        if never_default is not None:
            menu.never_default = True

        if shift_click is not None:
            menu.shift_click = True

        if no_working_directory is not None:
            menu.no_working_directory = True

        if position is not None:
            menu.position = position.position

        if separator is not None:
            menu.separator = separator.location

        if note is not None:
            menu.note = note.note

        if command is not None:
            menu.command = command.command

        if selection_limit is not None:
            menu.selection_limit = 1 if selection_limit.model == "Single" else 15 if selection_limit.model == "Document" else 100

        if has_lua_shield is not None:
            menu.has_lua_shield = True

        if disabled:
           menu.disabled = True

        if applies_to is not None:
            menu.condition = Condition(custom_aqs_condition=applies_to.aqs_condition)

        if fallback_display_text is not None:
            menu.display_text = fallback_display_text.text

        if display_text is not None:
            menu.display_text = display_text.text
