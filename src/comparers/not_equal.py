from dataclasses import dataclass

from src.comparers.icomparer import IComparer


@dataclass
class NotEqual(IComparer):
    to: str | int | float

    def to_aqs_string(self) -> str:
        # Looks like :<>{val}
        if isinstance(self.to, str):
            return f':<>"{self.to}"'
        return f":<>{self.to}"
