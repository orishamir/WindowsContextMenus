from dataclasses import dataclass

from context_menu_toolkit.registry.aqs_conditions.iaqscondition import IAqsCondition


@dataclass
class AqsAnd(IAqsCondition):
    conditions: list[IAqsCondition]

    def to_aqs_string(self) -> str:
        conditions_as_str = (condition.to_aqs_string() for condition in self.conditions)
        chained_ands = " AND ".join(conditions_as_str)
        return f"({chained_ands})"


@dataclass
class AqsNot(IAqsCondition):
    condition: IAqsCondition

    def to_aqs_string(self) -> str:
        return f"(NOT {self.condition.to_aqs_string()})"


@dataclass
class AqsOr(IAqsCondition):
    conditions: list[IAqsCondition]

    def to_aqs_string(self) -> str:
        conditions_as_str = (condition.to_aqs_string() for condition in self.conditions)
        chained_ors = " OR ".join(conditions_as_str)
        return f"({chained_ors})"
