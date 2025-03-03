from dataclasses import dataclass

from context_menu_toolkit.comparers import IComparer
from context_menu_toolkit.conditions.base_class.condition_base_class import ConditionBase

PROPERTY_NAME = "System.FileName"


@dataclass
class FileName(ConditionBase):
    """This condition checks the name of the file, including extension.

    Reference:
        [MSDN - System.FileName](https://learn.microsoft.com/en-us/windows/win32/properties/props-system-filename)
    """
    comparer: IComparer

    def to_aqs_string(self) -> str:
        return f"({PROPERTY_NAME}{self.comparer.to_aqs_string()})"
