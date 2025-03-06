from dataclasses import dataclass

from context_menu_toolkit.conditions.base_class.condition_base_class import ConditionBase
from context_menu_toolkit.conditions.comparison_type import ComparisonType

PROPERTY_NAME = "System.FileExtension"


@dataclass
class ExtensionType(ConditionBase):
    """Checks the extension of the file. Should include the leading period.

    Reference:
        [MSDN - System.FileExtension](https://learn.microsoft.com/en-us/windows/win32/properties/props-system-fileextension)
    """
    extension: str
    comparison: ComparisonType

    def to_aqs_string(self) -> str:
        return f"({PROPERTY_NAME}:{self.comparison}{self.extension})"
