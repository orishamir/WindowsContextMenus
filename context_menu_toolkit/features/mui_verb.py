from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class MUIVerb(IFeature):
    """Defines the displayed text of the context menu, i.e. the text that appears on right click.

    Attributes:
        name: The text that should be displayed for the context menu on right-click.
              You can also use string localization, which tells Windows to look up a string resource from a DLL (or EXE) file.
              For example `MUIVerb=@shell32.dll,-8518` -> `"Send To"`
    """

    name: str

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="MUIVerb", type=DataType.REG_SZ, data=self.name),
        )
