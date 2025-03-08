from enum import StrEnum


class ComparisonType(StrEnum):
    """Comparison types, such as ==, !=, <=, etc.

    Todo:
        how to handle str/int differences?
        ```python
            if isinstance(self.to, str):
                return f':<>"{self.to}"'
            return f":<>{self.to}"
        ```

    References:
        [MSDN - Using Advanced Query Syntax Programmatically - Query Operators](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators)
    """

    CONTAINS = "~="
    """Compares using contains operator for strings."""

    DOS_WILDCARD = "~"
    """Compares using DOS-style wildcard characters.

    ? matches one arbitrary character.
    * matches zero or more arbitrary characters.

    Example:
        "Mic?osoft W*d" - Finds files where the file name starts with "Mic", followed by some character,
                          followed by "osoft w", followed by any characters ending with d.
    """

    ENDS_WITH = "~>"
    """Compares using endswith operator for strings."""

    EQUALS = "="
    """Compares using equals."""

    GREATER_THAN = ">"
    """Compares greater than."""

    GREATER_THAN_EQUAL = ">="
    """Compares using greater than equals."""

    LESS_THAN = "<"
    """Compares using less than."""

    LESS_THAN_EQUAL = "<="
    """Compares using less than equals."""

    NOT_EQUAL = "<>"
    """Compares using not equals."""

    STARTS_WITH = "~<"
    """Compares using startswith operator for strings."""
