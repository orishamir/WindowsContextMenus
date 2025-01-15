"""
Choose in what condition should the
context menu item be displayed

Sources:
    [1] https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax
"""
from dataclasses import dataclass

from src.conditions import ICondition
from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType

CONDITION_VALUE = "AppliesTo"


@dataclass
class ConditionFeature(IFeature):
    condition: ICondition

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name=CONDITION_VALUE, type=DataType.REG_SZ, data=self.condition.to_aqs_string())
        )
