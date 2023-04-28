"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax
"""

from src.conditions import ICondition
from src.features import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType

CONDITION_VALUE = "AppliesTo"


class Condition(IFeature):
    def __init__(self, condition: ICondition):
        self.condition = condition

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(CONDITION_VALUE, ValueType.REG_SZ, self.condition.to_aqs_string())
        )
