from typing import Protocol


class ICondition(Protocol):
    """This is the interface that all conditions should implement.
    Conditions' syntax is "Advanced Query Syntax" (AQS)

    References:
        [MSDN - Advanced Query Syntax](https://learn.microsoft.com/en-us/windows/win32/lwef/-search-2x-wds-aqsreference)

        [MSDN - Using Advanced Query Syntax Programmatically](https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax)

        [Some available conditions](https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85))
    """

    def to_aqs_string(self) -> str:
        """Convert the condition to its actual
        Advanced Query Standard (aqs) representation.
        """
        raise NotImplementedError("Conditions should implement their own to_string() method.")
