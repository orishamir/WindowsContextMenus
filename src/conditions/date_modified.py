from datetime import date as Date

from src.conditions.base_class.condition_base_class import ConditionBase
from src.operators import IOperator, Equal

PROPERTY_NAME = "System.DateModified"


class DateModified(ConditionBase):
    """
    This condition checks the modification date of the file.
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
