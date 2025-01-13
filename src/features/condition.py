"""
Choose in what condition should the
context menu item be displayed

Sources:
    [1] https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax
"""

from src.conditions import ICondition
from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType

CONDITION_VALUE = "AppliesTo"


class Condition(IFeature):
    def __init__(self, condition: ICondition):
        self.condition = condition

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(CONDITION_VALUE, DataType.REG_SZ, self.condition.to_aqs_string())
        )
