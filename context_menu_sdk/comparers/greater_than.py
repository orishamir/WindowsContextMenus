from dataclasses import dataclass

from context_menu_sdk.comparers.icomparer import IComparer


@dataclass
class GreaterThan(IComparer):
    than: str | int | float

    def to_aqs_string(self) -> str:
        return f":>{self.than}"
