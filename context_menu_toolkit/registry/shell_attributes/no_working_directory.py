from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "NoWorkingDirectory"


@dataclass
class NoWorkingDirectory(IShellAttribute):
    r"""Don't use the clicked item's working directory path when opening the context menu item.

    Normally, Windows sets the working directory to the folder containing the file/folder/etc you clicked on.
    This can sometimes lead to unintended behavior if the program being launched makes assumptions about its working directory.

    By setting NoWorkingDirectory, Windows skips setting the working directory, and the program will inherit the default working directory (often C:\Windows\System32 or whatever the default is for the parent process).

    References:
        <https://superuser.com/questions/703275/whats-the-meaning-of-noworkingdirectory-string-value-in-windows-registry>
    """

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_SZ, data=""),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "NoWorkingDirectory | None":
        if tree.contains_value(ATTRIBUTE_NAME):
            return NoWorkingDirectory()
        return None
