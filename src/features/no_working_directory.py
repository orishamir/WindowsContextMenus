"""
Source:
    https://superuser.com/questions/703275/whats-the-meaning-of-noworkingdirectory-string-value-in-windows-registry
"""

from src.features import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType

NO_WORKING_DIRECTORY_VALUE = "NoWorkingDirectory"


class NoWorkingDirectory(IFeature):
    """
    Don't copy the current working directory path when
    opening the context menu item.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(NO_WORKING_DIRECTORY_VALUE, ValueType.REG_SZ, "")
        )
