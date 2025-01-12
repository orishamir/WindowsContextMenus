from src.comparers import IComparer
from src.conditions.base_class.condition_base_class import ConditionBase

PROPERTY_NAME = "System.FileExtension"


class ExtensionType(ConditionBase):
    """
    This condition checks the value of the extension of the file.
    Should include the leading period.
    
    Reference:
        https://learn.microsoft.com/en-us/windows/win32/properties/props-system-fileextension
    """

    def __init__(self, operator: IComparer):
        if not isinstance(operator, IComparer):
            raise TypeError(f"Operator should be of type IOperator. Not {type(operator)}")

        self.operator = operator

    def to_aqs_string(self) -> str:
        return f"({PROPERTY_NAME}{self.operator.to_aqs_string()})"
