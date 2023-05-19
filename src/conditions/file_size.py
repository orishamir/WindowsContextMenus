from src.conditions.base_class.condition_base_class import ConditionBase
from src.conditions.operators import IOperator, Equal

PROPERTY_NAME = "System.Size"


class FileSize(ConditionBase):
    """
    This condition checks the size of the file.
    """

    def __init__(self, size: str | int | IOperator):
        if isinstance(size, str | int):
            size = Equal(size)

        if not isinstance(size, IOperator):
            raise TypeError(f"Size should either be a string, int, or an operator. Not {type(size)}")

        self.size = size

    def to_aqs_string(self) -> str:
        """
        Convert condition to its AQS representation.
        """

        return f"({PROPERTY_NAME}{self.size.to_aqs_string()})"
