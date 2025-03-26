from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class DisplayText(IShellAttribute):
    """Defines the displayed text of the context menu, i.e. the text that appears on right click.

    Attributes:
        text: The text that should be displayed for the context menu on right-click.
              You can also use string localization, which tells Windows to look up a string resource from a DLL (or EXE) file.
              For example `MUIVerb=@shell32.dll,-8518` -> `"Send To"`
    """
    text: str

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="MUIVerb", type=DataType.REG_SZ, data=self.text),
        )
