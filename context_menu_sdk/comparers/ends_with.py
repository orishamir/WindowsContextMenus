from dataclasses import dataclass

from context_menu_sdk.comparers.icomparer import IComparer


@dataclass
class EndsWith(IComparer):
    ends_with: str

    def to_aqs_string(self) -> str:
        return f":~>{self.ends_with}"
