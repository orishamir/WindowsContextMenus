from dataclasses import dataclass

from context_menu_sdk.conditions.base_class.condition_base_class import ConditionBase


@dataclass
class CustomCondition(ConditionBase):
    """
    This condition does not check anything, rather gives the user to
    choose a custom Condition if the built-it Conditions aren't sufficient.
    """
    aqs_condition: str

    def to_aqs_string(self) -> str:
        return f"({self.aqs_condition})"
