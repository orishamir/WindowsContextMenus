from __future__ import annotations

from enum import StrEnum
from typing import Any, Optional

from pydantic import BaseModel


class ContextMenuForm(BaseModel):
    name: str
    exec: str
    icon: str
    shift_click: bool
    disabled: bool
    conditions: list[ConditionForm]


class ConditionForm(BaseModel):
    type: Optional[ConditionType] = None
    comparer: Optional[ComparerType] = None
    value: Optional[Any] = None


class ConditionType(StrEnum):
    FILE_NAME = "File name"
    FILE_SIZE = "File size"
    EXTENSION = "Extension"


class ComparerType(StrEnum):
    LESS_THAN = "Less than"
    LESS_THAN_EQUALS = "Less than equal"
    GREATER_THAN = "Greater than"
    GREATER_THAN_EQUALS = "Greater than equal"
    EQUALS = "Equals"
    STARTS_WITH = "Starts with"
    ENDS_WITH = "Ends with"
    CONTAINS = "Contains"
    WILDCARD = "Wildcard"


CONDITION_TYPE_TO_COMPARER: dict[ConditionType, list[ComparerType]] = {
    ConditionType.EXTENSION: [
        ComparerType.EQUALS,
        ComparerType.CONTAINS,
        ComparerType.STARTS_WITH,
        ComparerType.ENDS_WITH,
        ComparerType.WILDCARD,
    ],
    ConditionType.FILE_NAME: [
        ComparerType.EQUALS,
        ComparerType.CONTAINS,
        ComparerType.STARTS_WITH,
        ComparerType.ENDS_WITH,
        ComparerType.WILDCARD,
    ],
    ConditionType.FILE_SIZE: [
        ComparerType.LESS_THAN,
        ComparerType.LESS_THAN_EQUALS,
        ComparerType.GREATER_THAN,
        ComparerType.GREATER_THAN_EQUALS,
        ComparerType.EQUALS,
    ],
}
