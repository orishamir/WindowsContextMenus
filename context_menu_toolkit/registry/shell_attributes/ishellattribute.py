from typing import Protocol

from context_menu_toolkit.registry.registry_structs.registry_key import RegistryKey


class IShellAttribute(Protocol):
    """This interface represents attributes for shell verbs (context menus). Examples include MUIVerb (display_text), Icon, etc."""

    def apply_registry(self, tree: RegistryKey) -> None:
        """Modify `tree` such that the attribute is applied."""
