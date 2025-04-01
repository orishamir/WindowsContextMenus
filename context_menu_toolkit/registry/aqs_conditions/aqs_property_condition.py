from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from context_menu_toolkit.registry.aqs_conditions.iaqscondition import IAqsCondition


@dataclass
class AqsPropertyCondition[T](IAqsCondition):
    """Condition based on metadata properties.

    Attributes:
        property: The metadata property to filter by.
        comparison: The comparison type.
        value: The value to filter against.

    Examples:
        System.FileExtension:=".mp4"  # Extension equals .mp4
        System.Size:>"20MB"  # File size is greater than 20MB

    References:
        [^1]: [MSDN - Advanced Query Syntax](https://learn.microsoft.com/en-us/windows/win32/lwef/-search-2x-wds-aqsreference)
        [^2]: [MSDN - Using Advanced Query Syntax Programmatically](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax)
        [^3]: [Some available conditions](https://learn.microsoft.com/en-us/windows/win32/properties/core-bumper)
    """

    property: AqsProperty
    comparison: ComparisonType
    value: T

    def to_aqs_string(self) -> str:
        """Convert the condition to its actual Advanced Query Standard (aqs) representation."""
        return f"{self.property}:{self.comparison}{self.value}"


class AqsProperty(StrEnum):
    """Some properties to filter by.

    References:
        [^1]: <https://learn.microsoft.com/en-us/windows/win32/properties/core-bumper>
    """

    FILE_NAME = "System.FileName"
    FILE_SIZE = "System.Size"
    FILE_EXTENSION = "System.FileExtension"


class ComparisonType(StrEnum):
    """Comparison types, such as ==, !=, <=, etc.

    References:
        [^1]: <https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators>
    """

    CONTAINS = "~="
    """Compares using contains operator for strings."""

    DOS_WILDCARD = "~"
    """Compares using DOS-style wildcard characters.

    ? matches one arbitrary character.
    * matches zero or more arbitrary characters.

    Example:
        "Mic?osoft W*d" - Finds files where the file name starts with "Mic", followed by some character,
                          followed by "osoft w", followed by any characters ending with d.
    """

    ENDS_WITH = "~>"
    """Compares using endswith operator for strings."""

    EQUALS = "="
    """Compares using equals."""

    GREATER_THAN = ">"
    """Compares greater than."""

    GREATER_THAN_EQUAL = ">="
    """Compares using greater than equals."""

    LESS_THAN = "<"
    """Compares using less than."""

    LESS_THAN_EQUAL = "<="
    """Compares using less than equals."""

    NOT_EQUAL = "<>"
    """Compares using not equals."""

    STARTS_WITH = "~<"
    """Compares using startswith operator for strings."""
