from abc import ABC, abstractmethod

from src.registry_structs.registry_key import RegistryKey


class IFeature(ABC):
    """
    This interface represents classes which are "features",
    i.e. somethingthat is added to the context menu
    """

    @abstractmethod
    def apply_to(self, tree: RegistryKey) -> None:
        """
        Change `tree` such that it contains the
        feature should it be applied to the registry.
        """

        raise NotImplementedError("Classes that realize IFeature must implement apply_to")
