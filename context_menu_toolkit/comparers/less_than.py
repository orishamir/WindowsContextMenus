from dataclasses import dataclass

from context_menu_toolkit.comparers.icomparer import IComparer


@dataclass
class LessThan(IComparer):
    """
    Compares using less than.

    References:
        [MSDN](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators)
    """
    than: str | int | float

    def to_aqs_string(self) -> str:
        return f":<{self.than}"
