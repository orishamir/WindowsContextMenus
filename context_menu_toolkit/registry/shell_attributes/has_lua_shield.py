from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "HasLUAShield"


@dataclass
class HasLuaShield(IShellAttribute):
    """Display a User Account Control (UAC) shield.

    Note:
        You can also use an Icon.

    References:
        <https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax>
    """

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_SZ, data=""),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "HasLuaShield | None":
        if tree.contains_value(ATTRIBUTE_NAME):
            return HasLuaShield()
        return None
