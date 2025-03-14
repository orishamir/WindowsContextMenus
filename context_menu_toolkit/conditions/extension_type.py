from dataclasses import dataclass

from context_menu_toolkit.conditions.base_class.condition_base_class import ConditionBase
from context_menu_toolkit.conditions.comparison_type import ComparisonType

PROPERTY_NAME = "System.FileExtension"


@dataclass
class ExtensionType(ConditionBase):
    """Checks the extension of the file. Should include the leading period.

    Attributes:
        comparison: The comparing method, such as ==, startswith, contains, etc.
        extension: The extension to compare against.

    Reference:
        [MSDN - System.FileExtension](https://learn.microsoft.com/en-us/windows/win32/properties/props-system-fileextension)
    """
    comparison: ComparisonType
    extension: str

    def __post_init__(self) -> None:
        """Make sure extension contains leading period."""
        self.extension = "." + self.extension.removeprefix(".")

    def to_aqs_string(self) -> str:
        return f'({PROPERTY_NAME}:{self.comparison}"{self.extension}")'
