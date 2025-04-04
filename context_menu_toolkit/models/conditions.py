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
    """Add a condition for when the context menu should appear. Resembels MongoDB-style query syntax.

    It is recommended to initialize from a dictionary.

    Example:
        ```python
        # Matches .mp4 files or files whose name start with "my".
        Condition.model_validate({
            "or": {
                "file_name": {
                    "startswith": "my",
                },
                "extension": {
                    "eq": ".mp4",
                },
            },
        })
        ```
    """

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
    """Filter based on file name.

    Example:
        ```python
        Condition.model_validate({
            "file_name": {
                "startswith": "my",
            },
        })
        ```
    """


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
    """Filter based on file extension.

    When comparing using startswith, equals, or not equals, a leading period (.) is required.
    """


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
    """Filter based on file size."""
