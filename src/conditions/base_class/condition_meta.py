from src.conditions.operators import (
    Equal,
    NotEqual,
    LessThan,
    LessThanEqual,
    GreaterThan,
    GreaterThanEqual,
    Contains
)
from src.conditions.base_class.icondition import ICondition


class ConditionMeta(type):
    """
    This is the metaclass for conditions, that's for the
    `==` or `!=` or `<=` functionality to work.

    For example:
    if ExtensionType's metaclass is ConditionBase, then that means:
        (ExtensionType != ".exe.")
    works and is equivalent to
        ExtensionType(NotEqual(".exe"))
    """

    def __eq__(cls, other: str | int | float) -> ICondition:
        return cls(Equal(other))

    def __ne__(cls, other: str | int | float) -> ICondition:
        return cls(NotEqual(other))

    def __lt__(cls, other: str | int | float) -> ICondition:
        return cls(LessThan(other))

    def __le__(cls, other: str | int | float) -> ICondition:
        return cls(LessThanEqual(other))

    def __gt__(cls, other: str | int | float) -> ICondition:
        return cls(GreaterThan(other))

    def __ge__(cls, other: str | int | float) -> ICondition:
        return cls(GreaterThanEqual(other))

    def __matmul__(cls, item: str) -> ICondition:
        return cls(Contains(item))

    def __rmatmul__(cls, item: str) -> ICondition:
        return cls(Contains(item))
