from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from context_menu_toolkit.registry.aqs_conditions.iaqscondition import IAqsCondition


@dataclass
class AqsPropertyCondition[T](IAqsCondition):
    property: AqsProperty
    comparison: ComparisonType
    value: T

    def to_aqs_string(self) -> str:
        """Convert the condition to its actual Advanced Query Standard (aqs) representation."""
        return f"{self.property}:{self.comparison}{self.value}"


class AqsProperty(StrEnum):
    FILE_NAME = "System.FileName"
    FILE_SIZE = "System.Size"
    FILE_EXTENSION = "System.FileExtension"


class ComparisonType(StrEnum):
    CONTAINS = "~="
    DOS_WILDCARD = "~"
    ENDS_WITH = "~>"
    EQUALS = "="
    GREATER_THAN = ">"
    GREATER_THAN_EQUAL = ">="
    LESS_THAN = "<"
    LESS_THAN_EQUAL = "<="
    NOT_EQUAL = "<>"
    STARTS_WITH = "~<"
