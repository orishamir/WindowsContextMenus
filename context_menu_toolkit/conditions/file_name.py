from dataclasses import dataclass

from context_menu_toolkit.conditions.base_class.condition_base_class import ConditionBase
from context_menu_toolkit.conditions.comparison_type import ComparisonType

PROPERTY_NAME = "System.FileName"


@dataclass
class FileName(ConditionBase):
    """This condition checks the name of the file, including extension.

    Attributes:
        comparison: The comparing method, such as ==, startswith, contains, etc.
        name: The name to compare against.

    Reference:
        [MSDN - System.FileName](https://learn.microsoft.com/en-us/windows/win32/properties/props-system-filename)
    """
    comparison: ComparisonType
    name: str

    def to_aqs_string(self) -> str:
        return f'({PROPERTY_NAME}:{self.comparison}"{self.name}")'
