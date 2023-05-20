from src.conditions.base_class.condition_base_class import ConditionBase


class CustomCondition(ConditionBase):
    """
    This condition does not check anything, rather gives the user to
    choose a custom Condition if the built-it Conditions aren't sufficient.
    """

    def __init__(self, aqs_condition: str):
        if not isinstance(aqs_condition, str):
            raise TypeError(f"Extension should either be a string. Not {type(aqs_condition)}")

        self.aqs_condition = aqs_condition

    def to_aqs_string(self) -> str:
        """
        Convert condition to its AQS representation.
        """

        return f"({self.aqs_condition})"
