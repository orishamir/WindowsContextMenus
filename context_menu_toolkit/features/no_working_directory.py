from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class NoWorkingDirectory(IFeature):
    """Don't copy the current working directory path when
    opening the context menu item.

    References:
        [Superuser - What's the meaning of "NoWorkingDirectory" string value in Windows Registry?](https://superuser.com/questions/703275/whats-the-meaning-of-noworkingdirectory-string-value-in-windows-registry)
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="NoWorkingDirectory", type=DataType.REG_SZ, data=""),
        )
