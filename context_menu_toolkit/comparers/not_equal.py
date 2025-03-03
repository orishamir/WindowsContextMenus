from dataclasses import dataclass

from context_menu_toolkit.comparers.icomparer import IComparer


@dataclass
class NotEqual(IComparer):
    """Compares using not equals.

    References:
        [MSDN](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators)
    """
    to: str | int | float

    def to_aqs_string(self) -> str:
        # Looks like :<>{val}
        if isinstance(self.to, str):
            return f':<>"{self.to}"'
        return f":<>{self.to}"
