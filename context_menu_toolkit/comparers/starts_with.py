from dataclasses import dataclass

from context_menu_toolkit.comparers.icomparer import IComparer


@dataclass
class StartsWith(IComparer):
    starts_with: str

    def to_aqs_string(self) -> str:
        return f":~<{self.starts_with}"
