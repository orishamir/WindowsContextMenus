from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass

from context_menu_toolkit.conditions.base_class.icondition import ICondition

AQS_OPERATOR_AND = " AND "
AQS_OPERATOR_OR = " OR "
AQS_OPERATOR_NOT = "NOT"


class ConditionBase:
    r"""Extends the ICondition interface by adding syntactic sugar definitions for instantiating Conditions.

    Also adds functionality for ==, !=, etc. for instantiating Conditions.

    Example:
        ```python
        ExtensionType != ".exe"
        # is equivalent to
        ExtensionType(NotEqual(".exe")

        ExtensionType(NotEqual(".exe")) & ExtensionType(NotEqual(".dll"))
        # is equivalent to
        And(
            ExtensionType(NotEqual(".exe")),
            ExtensionType(NotEqual(".dll")),
        )
        ```
        Should both be True, given that ExtensionType inherits from ConditionBase
    """

    @abstractmethod
    def to_aqs_string(self) -> str:
        """Convert the condition to its actual Advanced Query Standard (aqs) representation."""
        raise NotImplementedError("Conditions should implement their own to_aqs_string() method.")

    def __and__(self: ICondition, other: ICondition) -> ConditionBase:
        return And([self, other])

    def __rand__(self: ICondition, other: ICondition) -> ConditionBase:
        return And([other, self])

    def __or__(self: ICondition, other: ICondition) -> ConditionBase:
        return Or([self, other])

    def __ror__(self: ICondition, other: ICondition) -> ConditionBase:
        return Or([other, self])

    def __invert__(self: ICondition) -> ConditionBase:
        return Not(self)


@dataclass
class And(ConditionBase):
    """The And operator between conditions.

    Example:
        ```python
        from context_menu_toolkit.comparers import GreaterThan, Equal
        from context_menu_toolkit.conditions import FileSize, ExtensionType

        And(
            conditions=[
                FileSize(GreaterThan("20MB")),
                ExtensionType(Equal(".pdf")),
            ],
        )
        ```
    """
    conditions: list[ICondition]

    def to_aqs_string(self) -> str:
        conditions_as_str = (condition.to_aqs_string() for condition in self.conditions)
        chained_ands = AQS_OPERATOR_AND.join(conditions_as_str)
        return f"({chained_ands})"


@dataclass
class Or(ConditionBase):
    """The Or operator between conditions.

    Example:
        ```python
        from context_menu_toolkit.comparers import GreaterThan, Equal
        from context_menu_toolkit.conditions import FileSize, ExtensionType

        Or(
            conditions=[
                ExtensionType(Equal(".png")),
                ExtensionType(Equal(".jpeg")),
                ExtensionType(Equal(".jpg")),
            ],
        )
        ```
    """
    conditions: list[ICondition]

    def to_aqs_string(self) -> str:
        conditions_as_str = (condition.to_aqs_string() for condition in self.conditions)
        chained_ors = AQS_OPERATOR_OR.join(conditions_as_str)
        return f"({chained_ors})"


@dataclass
class Not(ConditionBase):
    """The Not operator of a condition.

    Example:
        ```python
        from context_menu_toolkit.comparers import GreaterThan, Equal
        from context_menu_toolkit.conditions import FileSize, ExtensionType
                Not(
            condition=ExtensionType(Equal(".png"))
        )
        ```
    """
    condition: ICondition

    def to_aqs_string(self) -> str:
        return f"({AQS_OPERATOR_NOT} {self.condition.to_aqs_string()})"
