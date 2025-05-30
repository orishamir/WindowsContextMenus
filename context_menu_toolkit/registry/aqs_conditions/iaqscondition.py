from typing import Protocol


class IAqsCondition(Protocol):
    """Represents a condition for when the context menu should show up.

    This is the interface that all conditions should implement.
    Conditions' syntax is "Advanced Query Syntax" (AQS).

    References:
        [^1]: <https://learn.microsoft.com/en-us/windows/win32/lwef/-search-2x-wds-aqsreference>
        [^2]: <https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax>
        [^3]: <https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)>
    """

    def to_aqs_string(self) -> str:
        """Convert the condition to its actual Advanced Query Standard (aqs) representation."""
        raise NotImplementedError("Aqs conditions should implement their own to_aqs_string() method.")
