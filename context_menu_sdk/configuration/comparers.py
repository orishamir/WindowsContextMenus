from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, field_validator, model_validator

from context_menu_sdk.configuration.custom_types import StrByteSize


class StartswithComparerConfig[T](BaseModel):
    startswith: Optional[T] = Field(None, alias="$startswith")


class EndswithComparerConfig[T](BaseModel):
    endswith: Optional[T] = Field(None, alias="$endswith")


class ContainsComparerConfig[T](BaseModel):
    contains: Optional[T] = Field(None, alias="$contains")


class EqualsComparerConfig[T](BaseModel):
    eq: Optional[T] = Field(None, alias="$eq")


class NotEqualsComparerConfig[T](BaseModel):
    ne: Optional[T] = Field(None, alias="$ne")


class LessThanComparerConfig[T](BaseModel):
    lt: Optional[T] = Field(None, alias="$lt")


class GreaterThanComparerConfig[T](BaseModel):
    gt: Optional[T] = Field(None, alias="$gt")


class LessThanEqualsComparerConfig[T](BaseModel):
    lte: Optional[T] = Field(None, alias="$lte")


class GreaterThanEqualsComparerConfig[T](BaseModel):
    gte: Optional[T] = Field(None, alias="$gte")


class WildcardComparerConfig[T](BaseModel):
    wildcard: Optional[T] = Field(None, alias="$wildcard")


class _ValidateOneOf(BaseModel, extra="forbid", populate_by_name=True):
    """
    A model for making sure at least one of the fields are set.
    For example, FileSize respects int, le, ge, etc.
    Any one of which can be None, but at least one of the fields should exist.
    """

    @model_validator(mode="after")
    def _inner_validator(self) -> _ValidateOneOf:
        if not self.model_fields_set:
            raise ValueError("no comparer provided. make sure you typed it correctly!")

        return self


class ExtensionComparerConfig(
    _ValidateOneOf,
    StartswithComparerConfig[str],
    EndswithComparerConfig[str],
    ContainsComparerConfig[str],
    EqualsComparerConfig[str],
    NotEqualsComparerConfig[str],
    WildcardComparerConfig[str],
):
    @field_validator("eq", "ne", "startswith")
    def _validate_extension_comma(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None

        if not value.startswith("."):
            raise ValueError("extension operator should contain comma when using eq, ne, startswith")

        return value


class FileNameComparerConfig(
    _ValidateOneOf,
    StartswithComparerConfig[str],
    EndswithComparerConfig[str],
    ContainsComparerConfig[str],
    EqualsComparerConfig[str],
    NotEqualsComparerConfig[str],
    WildcardComparerConfig[str],
):
    pass


class FileSizeComparerConfig(
    _ValidateOneOf,
    EqualsComparerConfig[StrByteSize],
    LessThanComparerConfig[StrByteSize],
    GreaterThanComparerConfig[StrByteSize],
    LessThanEqualsComparerConfig[StrByteSize],
    GreaterThanEqualsComparerConfig[StrByteSize],
    NotEqualsComparerConfig[StrByteSize],
):
    @model_validator(mode="after")
    def _validate_non_conflicting_values(self) -> FileSizeComparerConfig:
        if self.lt and self.gt:
            if self.lt > self.gt:
                raise ValueError("conflicting values for less-than and greater-than")

        if self.lte and self.gte:
            if self.lt >= self.gt:
                raise ValueError("conflicting values for less-than and greater-than")

        return self
