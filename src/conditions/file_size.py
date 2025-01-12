from src.conditions.base_class.condition_base_class import ConditionBase
from src.comparers import IComparer

PROPERTY_NAME = "System.Size"


class FileSize(ConditionBase):
    """
    This condition checks the size of the file.
    
    Example:
        System.Size:<30MB      - Size less than 30 megabytes
        System.Size:<30000000  - Size less than 30 megabytes
    
    Reference:
        https://learn.microsoft.com/en-us/windows/win32/properties/props-system-size
    """

    def __init__(self, operator: IComparer):
        if not isinstance(operator, IComparer):
            raise TypeError(f"Operator should be of type IOperator. Not {type(operator)}")

        self.operator = operator

    def to_aqs_string(self) -> str:
        return f"({PROPERTY_NAME}{self.operator.to_aqs_string()})"
