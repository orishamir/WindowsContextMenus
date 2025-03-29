from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs.registry_key import RegistryKey
from context_menu_toolkit.registry.registry_structs.registry_value import DataType, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

COMMAND_KEY_NAME = "command"
DEFAULT_VALUE = ""


@dataclass
class Command(IShellAttribute):
    r"""Add a command that gets executed when clicking the context menu.

    Attributes:
        command: The command to run, can contain CommandPlaceholders.

    Example:
        ```python
        # convert passed file to mp4
        Command(f'cmd.exe /c ffmpeg -i "{CommandPlaceholder.FIRST_SELECTED}" "{CommandPlaceholder.FIRST_SELECTED}".mp4')
        # start command prompt in the working directory
        Command(f'cmd.exe /d /k "{CommandPlaceholder.WORKING_DIRECTORY}"')
        ```

    """

    command: str

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_subkey(
            RegistryKey(
                name=COMMAND_KEY_NAME,
                values=[
                    RegistryValue(name=DEFAULT_VALUE, type=DataType.REG_SZ, data=self.command),
                ],
            ),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "Command | None":
        subkey = tree.get_subkey(COMMAND_KEY_NAME)
        if subkey is None:
            return None

        value = subkey.get_value(DEFAULT_VALUE)
        if value is not None and isinstance(value.data, str):
            return Command(value.data)
        return None
