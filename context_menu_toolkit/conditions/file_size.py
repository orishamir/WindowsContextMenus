from dataclasses import dataclass

from context_menu_toolkit.conditions.base_class.condition_base_class import ConditionBase
from context_menu_toolkit.conditions.comparison_type import ComparisonType

PROPERTY_NAME = "System.Size"


@dataclass
class FileSize(ConditionBase):
    """This condition checks the size of the file.

    Attributes:
        comparison: The comparing method, such as >, <=, etc.
        size: The size to compare against. In the format "30MB".

    Example:
        ```
        System.Size:<30MB      - Size less than 30 megabytes
        System.Size:<30000000  - Size less than 30 megabytes
        ```

    References:
        [MSDN - System.Size](https://learn.microsoft.com/en-us/windows/win32/properties/props-system-size)
    """

    comparison: ComparisonType
    size: str

    def to_aqs_string(self) -> str:
        """Convert file size to Advanced Query Syntax representation.

        Example:
            "System.Size:<30MB"
        """
        return f"({PROPERTY_NAME}:{self.comparison}{self.size})"
