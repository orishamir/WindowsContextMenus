from src.conditions.base_class.condition_base_class import ConditionBase
from src.operators import IOperator, Equal

PROPERTY_NAME = "System.FileName"


class FileName(ConditionBase):
    """
    This condition checks the name of the file.
    """

    def __init__(self, name: str | IOperator):
        if isinstance(name, str):
            name = Equal(name)

        if not isinstance(name, IOperator):
            raise TypeError(f"name should be a string. Not {type(name)}")

        self.name = name

    def to_aqs_string(self) -> str:
        """
        Convert condition to its AQS representation.
        """

        return f"({PROPERTY_NAME}{self.name.to_aqs_string()})"
