from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs.registry_key import RegistryKey
from context_menu_toolkit.registry_structs.registry_value import DataType, RegistryValue

COMMAND_KEY_NAME = "command"
DEFAULT_VALUE = ""


@dataclass
class Command(IFeature):
    """Add a command that gets executed when clicking the context menu.

    TODO: Improve API here, allowing for easy path parameters.
          for example, there exists both %V and %1.
    """
    command: str

    def apply_to(self, tree: RegistryKey) -> None:
        tree.subkeys.append(
            RegistryKey(name=COMMAND_KEY_NAME, values=[
                RegistryValue(name=DEFAULT_VALUE, type=DataType.REG_SZ, data=self.command),
            ]),
        )
