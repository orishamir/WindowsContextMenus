from dataclasses import dataclass

from context_menu_toolkit.comparers.icomparer import IComparer


@dataclass
class Contains(IComparer):
    substr: str

    def to_aqs_string(self) -> str:
        return f":~={self.substr}"
