from dataclasses import dataclass

from context_menu_toolkit.comparers.icomparer import IComparer


@dataclass
class StartsWith(IComparer):
    """
    Compares using startswith operator for strings.

    References:
        [MSDN](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators)
    """
    starts_with: str

    def to_aqs_string(self) -> str:
        return f":~<{self.starts_with}"
