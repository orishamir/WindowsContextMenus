from pydantic import BaseModel, Field


class EqualsComparison[T](BaseModel):
    eq: T | None = None


class NotEqualsComparison[T](BaseModel):
    ne: T | None = None


class ContainsComparison[T](BaseModel):
    contains: T | None = None


class StartswithComparison[T](BaseModel):
    startswith: T | None = None


class EndswithComparison[T](BaseModel):
    endswith: T | None = None


class GreaterThanComparison[T](BaseModel):
    gt: T | None = None


class GreaterThanEqualsComparison[T](BaseModel):
    gte: T | None = None


class LessThanComparison[T](BaseModel):
    lt: T | None = None


class LessThanEqualsComparison[T](BaseModel):
    lte: T | None = None


class DosWildcardComparison[T](BaseModel):
    wildcard: T | None = None


class InComparison[T](BaseModel):
    in_: list[T] | None = Field(default=None, alias="in")


class NinComparison[T](BaseModel):
    nin: list[T] | None = None
