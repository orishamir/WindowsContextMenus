from dataclasses import dataclass

from context_menu_toolkit.conditions.base_class.condition_base_class import ConditionBase


@dataclass
class CustomCondition(ConditionBase):
    """Custom Condition in the Advanced Query Standard (aqs) representation."""

    aqs_condition: str

    def to_aqs_string(self) -> str:
        return f"({self.aqs_condition})"
