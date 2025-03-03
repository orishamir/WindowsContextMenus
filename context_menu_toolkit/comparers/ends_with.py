from dataclasses import dataclass

from context_menu_toolkit.comparers.icomparer import IComparer


@dataclass
class EndsWith(IComparer):
    """Compares using endswith operator for strings.

    References:
        [MSDN](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators)
    """
    ends_with: str

    def to_aqs_string(self) -> str:
        return f":~>{self.ends_with}"
