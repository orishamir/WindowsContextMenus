from typing import Protocol

from context_menu_toolkit.registry_structs.registry_key import RegistryKey


class IFeature(Protocol):
    """This interface represents classes which are "features", i.e. something that is added to the context menu."""

    def apply_to(self, tree: RegistryKey) -> None:
        """Modify `tree` such that the feature is applied."""
        raise NotImplementedError("Classes that realize IFeature must implement apply_to")
