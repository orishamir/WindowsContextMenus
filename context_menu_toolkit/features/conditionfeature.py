from dataclasses import dataclass

from context_menu_toolkit.conditions import ICondition
from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class ConditionFeature(IFeature):
    """Add a condition for the context menu to display.

    See context_menu_toolkit.conditions for available conditions.

    References:
        [MSDN - Getting Dynamic Behavior for Static Verbs by Using Advanced Query Syntax](https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax)

    Example:
        ```python
        from context_menu_toolkit.comparers import GreaterThan
        from context_menu_toolkit.conditions import FileSize

        ConditionFeature(
            condition=FileSize(
                comparer=GreaterThan("20MB"),
            ),
        )
        ```
    """

    condition: ICondition

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="AppliesTo", type=DataType.REG_SZ, data=self.condition.to_aqs_string()),
        )
