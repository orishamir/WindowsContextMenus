from dataclasses import dataclass

from src.comparers.icomparer import IComparer


@dataclass
class Equal(IComparer):
    to: str | int | float

    def to_aqs_string(self) -> str:
        if isinstance(self.to, str):
            return f':="{self.to}"'
        return f":={self.to}"
