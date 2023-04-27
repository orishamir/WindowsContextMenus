from src.registry_structs.registry_key import RegistryKey
from src.features.ifeature import IFeature
from src.registry_structs.registry_value import RegistryValue, ValueType

COMMAND_KEY_NAME = "command"


class Command(IFeature):
    """
    This feature determines which command gets
    executed on-click of the context menu item.
    """

    def __init__(self, command: str):
        self.command = command

    def apply_to(self, tree: RegistryKey) -> None:
        tree.subkeys.append(
            RegistryKey(COMMAND_KEY_NAME, [
                RegistryValue("", ValueType.REG_SZ, self.command)
            ])
        )
