"""
Source:
    https://superuser.com/questions/703275/whats-the-meaning-of-noworkingdirectory-string-value-in-windows-registry
"""
from dataclasses import dataclass

from context_menu_sdk.features.ifeature import IFeature
from context_menu_sdk.registry_structs import RegistryKey, RegistryValue, DataType

NO_WORKING_DIRECTORY_VALUE = "NoWorkingDirectory"


@dataclass
class NoWorkingDirectory(IFeature):
    """
    Don't copy the current working directory path when
    opening the context menu item.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name=NO_WORKING_DIRECTORY_VALUE, type=DataType.REG_SZ, data="")
        )
