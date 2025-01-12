from __future__ import annotations

from abc import abstractmethod

from src.conditions.base_class.condition_meta import ConditionMeta
from src.conditions.base_class.icondition import ICondition

AQS_OPERATOR_AND = " AND "
AQS_OPERATOR_OR = " OR "
AQS_OPERATOR_NOT = "NOT"


class ConditionBase(metaclass=ConditionMeta):
    """
    This base class extends the ICondition interface by adding
    definition for &, |, etc.
    It also makes that every class that inherits from it
    is automatically implementing ==, !=, etc. as a way to initialize it.

    For example:
        if ExtensionType inherits from ConditionBase,
        then that means:
            (ExtensionType != ".exe.")
            is equivalent to
            ExtensionType(NotEqual(".exe"))
        and that
            ExtensionType(NotEqual(".exe")) & ExtensionType(NotEqual(".dll"))
            is equivalent to
            And(
                ExtensionType(NotEqual(".exe")),
                ExtensionType(NotEqual(".dll"))
            )
    """

    @abstractmethod
    def to_aqs_string(self) -> str:
        """
        Convert the condition to its actual
        Advanced Query Standard (aqs) representation.
        """

        raise NotImplementedError("Conditions should implement their own to_aqs_string() method.")

    def __and__(self: ICondition, other: ICondition) -> ConditionBase:
        return And(self, other)

    def __rand__(self: ICondition, other: ICondition) -> ConditionBase:
        return And(other, self)

    def __or__(self: ICondition, other: ICondition) -> ConditionBase:
        return Or(self, other)

    def __ror__(self: ICondition, other: ICondition) -> ConditionBase:
        return Or(other, self)

    def __invert__(self: ICondition) -> ConditionBase:
        return Not(self)


class And(ConditionBase):
    def __init__(self, *conditions: ICondition):
        self.conditions = conditions

    def to_aqs_string(self) -> str:
        conditions_as_str = (condition.to_aqs_string() for condition in self.conditions)
        chained_ands = AQS_OPERATOR_AND.join(conditions_as_str)
        return f"({chained_ands})"


class Or(ConditionBase):
    def __init__(self, *conditions: ICondition):
        self.conditions = conditions

    def to_aqs_string(self) -> str:
        conditions_as_str = (condition.to_aqs_string() for condition in self.conditions)
        chained_ors = AQS_OPERATOR_OR.join(conditions_as_str)
        return f"({chained_ors})"


class Not(ConditionBase):
    def __init__(self, condition: ICondition):
        self.condition = condition

    def to_aqs_string(self) -> str:
        return f"({AQS_OPERATOR_NOT} {self.condition.to_aqs_string()})"
