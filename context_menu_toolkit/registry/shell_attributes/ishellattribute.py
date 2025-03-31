from typing import Protocol

from context_menu_toolkit.registry.registry_structs.registry_key import RegistryKey


class IShellAttribute(Protocol):
    """This interface represents attributes for shell verbs (context menus). Examples include MUIVerb (display_text), Icon, etc."""

    def apply_to_tree(self, tree: RegistryKey) -> None:
        """Modify `tree` such that the attribute is applied."""

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "IShellAttribute | None":
        """Create the shell attribute from a RegistryKey tree."""
