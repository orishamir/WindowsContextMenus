from dataclasses import dataclass

from src.comparers import IComparer
from src.conditions.base_class.condition_base_class import ConditionBase

PROPERTY_NAME = "System.FileExtension"


@dataclass
class ExtensionType(ConditionBase):
    """
    This condition checks the value of the extension of the file.
    Should include the leading period.
    
    Reference:
        https://learn.microsoft.com/en-us/windows/win32/properties/props-system-fileextension
    """
    comparer: IComparer

    def to_aqs_string(self) -> str:
        return f"({PROPERTY_NAME}{self.comparer.to_aqs_string()})"
