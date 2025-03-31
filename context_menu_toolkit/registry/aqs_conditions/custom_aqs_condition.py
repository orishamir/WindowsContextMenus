from dataclasses import dataclass

from context_menu_toolkit.registry.aqs_conditions.iaqscondition import IAqsCondition


@dataclass
class CustomAqsCondition(IAqsCondition):
    condition: str

    def to_aqs_string(self) -> str:
        return f"({self.condition})"
