from __future__ import annotations

from pydantic import BaseModel, Field

from context_menu_toolkit.models.condition_comparisons import (
    ContainsComparison,
    DosWildcardComparison,
    EndswithComparison,
    EqualsComparison,
    GreaterThanComparison,
    GreaterThanEqualsComparison,
    InComparison,
    LessThanComparison,
    LessThanEqualsComparison,
    NinComparison,
    NotEqualsComparison,
    StartswithComparison,
)


class Condition(BaseModel, extra="forbid"):
    file_name: FileNameComparison | None = None
    extension: ExtensionComparison | None = None
    file_size: FileSizeComparison | None = None
    custom_aqs_condition: str | None = None
    and_: list[Condition] | None = Field(default=None, alias="and")
    not_: Condition | None = Field(default=None, alias="not")
    nor: list[Condition] | None = None
    or_: list[Condition] | None = Field(default=None, alias="or")


class FileNameComparison(
    EqualsComparison[str],
    NotEqualsComparison[str],
    ContainsComparison[str],
    StartswithComparison[str],
    EndswithComparison[str],
    DosWildcardComparison[str],
    InComparison[str],
    NinComparison[str],
    extra="forbid",
):
    pass


class ExtensionComparison(
    EqualsComparison[str],
    NotEqualsComparison[str],
    ContainsComparison[str],
    StartswithComparison[str],
    EndswithComparison[str],
    DosWildcardComparison[str],
    InComparison[str],
    NinComparison[str],
    extra="forbid",
):
    pass


class FileSizeComparison(
    EqualsComparison[int],
    NotEqualsComparison[int],
    GreaterThanComparison[int],
    GreaterThanEqualsComparison[int],
    LessThanComparison[int],
    LessThanEqualsComparison[int],
    NinComparison[int],
    extra="forbid",
):
    pass
