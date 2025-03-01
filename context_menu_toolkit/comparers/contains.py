from dataclasses import dataclass

from context_menu_toolkit.comparers.icomparer import IComparer


@dataclass
class Contains(IComparer):
    """
    Compares using contains operator for strings.

    References:
        https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators
    """
    substr: str

    def to_aqs_string(self) -> str:
        return f":~={self.substr}"
