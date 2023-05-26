from src.conditions.base_class.condition_base_class import ConditionBase
from operators import IOperator, Equal
from datetime import date as Date

PROPERTY_NAME = "System.DateCreated"


class DateCreated(ConditionBase):
    """
    This condition checks the creation date of the file.
    """

    def __init__(self, date: str | Date | IOperator):
        if isinstance(date, str | Date):
            date = Equal(date)

        if not isinstance(date, IOperator):
            raise TypeError(f"date should be a string. Not {type(date)}")

        self.date = date

    def to_aqs_string(self) -> str:
        """
        Convert condition to its AQS representation.
        """

        return f"({PROPERTY_NAME}{self.date.to_aqs_string()})"
