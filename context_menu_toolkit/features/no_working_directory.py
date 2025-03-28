from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class NoWorkingDirectory(IFeature):
    r"""Don't use the clicked item's working directory path when opening the context menu item.

    Normally, Windows sets the working directory to the folder containing the file/folder/etc you clicked on.
    This can sometimes lead to unintended behavior if the program being launched makes assumptions about its working directory.

    By setting NoWorkingDirectory, Windows skips setting the working directory, and the program will inherit the default working directory (often C:\Windows\System32 or whatever the default is for the parent process).

    References:
        <https://superuser.com/questions/703275/whats-the-meaning-of-noworkingdirectory-string-value-in-windows-registry>
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="NoWorkingDirectory", type=DataType.REG_SZ, data=""),
        )
