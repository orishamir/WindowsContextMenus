from dataclasses import dataclass

from windows_context_menus.registry.aqs_conditions.iaqscondition import IAqsCondition


@dataclass
class CustomAqsCondition(IAqsCondition):
    """Freestyle Advanced Query Syntax string, for representing custom conditions which are not supported."""

    condition: str

    def to_aqs_string(self) -> str:
        return f"({self.condition})"
