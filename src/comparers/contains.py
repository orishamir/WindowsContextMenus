from dataclasses import dataclass

from src.comparers.icomparer import IComparer


@dataclass
class Contains(IComparer):
    substr: str

    def to_aqs_string(self) -> str:
        return f"~={self.substr}"
