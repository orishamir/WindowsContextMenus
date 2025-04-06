from typing import Protocol


class IAqsCondition(Protocol):
    """Represents a condition for when the context menu should show up.

    This is the interface that all conditions should implement.
    Conditions' syntax is "Advanced Query Syntax" (AQS).

    References:
        [^1]: [MSDN - Advanced Query Syntax](https://learn.microsoft.com/en-us/windows/win32/lwef/-search-2x-wds-aqsreference)
        [^2]: [MSDN - Using Advanced Query Syntax Programmatically](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax)
        [^3]: [Some available conditions](https://learn.microsoft.com/en-us/windows/win32/properties/core-bumper)
    """

    def to_aqs_string(self) -> str:
        """Convert the condition to its actual Advanced Query Standard (aqs) representation."""
        raise NotImplementedError("Aqs conditions should implement their own to_aqs_string() method.")
