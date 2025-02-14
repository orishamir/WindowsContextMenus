from dataclasses import dataclass

from context_menu_toolkit.comparers.icomparer import IComparer


@dataclass
class LessThanEqual(IComparer):
    than: str | int | float

    def to_aqs_string(self) -> str:
        return f":<={self.than}"
