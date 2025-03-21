from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class HasLuaShield(IFeature):
    """Display a User Account Control (UAC) shield.

    Note:
        You can also use an Icon.

    References:
        <https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax>
    """

    def apply_registry(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="HasLUAShield", type=DataType.REG_SZ, data=""),
        )
