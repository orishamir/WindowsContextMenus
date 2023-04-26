from abc import ABC, abstractmethod

from src.registry_structs.registry_key import RegistryKey


class IFeature(ABC):
    @abstractmethod
    def apply_to(self, tree: RegistryKey) -> None:
        raise NotImplementedError("Classes that realize IFeature must implement apply_to")
