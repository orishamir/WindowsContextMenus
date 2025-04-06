from dataclasses import dataclass

from context_menu_toolkit.registry.aqs_conditions.iaqscondition import IAqsCondition


@dataclass
class CustomAqsCondition(IAqsCondition):
    """Freestyle Advanced Query Syntax string, for representing custom conditions which are not supported."""

    condition: str

    def to_aqs_string(self) -> str:
        return f"({self.condition})"
