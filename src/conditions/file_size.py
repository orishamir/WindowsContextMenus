from dataclasses import dataclass

from src.comparers import IComparer
from src.conditions.base_class.condition_base_class import ConditionBase

PROPERTY_NAME = "System.Size"


@dataclass
class FileSize(ConditionBase):
    """
    This condition checks the size of the file.
    
    Example:
        System.Size:<30MB      - Size less than 30 megabytes
        System.Size:<30000000  - Size less than 30 megabytes
    
    Reference:
        https://learn.microsoft.com/en-us/windows/win32/properties/props-system-size
    """
    comparer: IComparer

    def to_aqs_string(self) -> str:
        return f"({PROPERTY_NAME}{self.comparer.to_aqs_string()})"
