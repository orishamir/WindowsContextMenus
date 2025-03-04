from typing import Protocol, runtime_checkable


@runtime_checkable
class IComparer(Protocol):
    """This interface represents a comparer type, such as ==, !=, <=, etc.

    For examples look at `context_menu_toolkit.comparers`.

    References:
        [MSDN](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators)
    """

    def to_aqs_string(self) -> str:
        """Convert this comparer to the equivalent Advanced Query Standard (aqs) string."""
        raise NotImplementedError("Comparers should implement their own to_aqs_string() method")
