"""
Conditions' syntax is "Advanced Query Syntax" (AQS)
https://learn.microsoft.com/en-us/windows/win32/lwef/-search-2x-wds-aqsreference

Some available ...:
https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""

from abc import ABC, abstractmethod


class ICondition(ABC):
    @abstractmethod
    def to_aqs_string(self) -> str:
        raise NotImplementedError("Conditions should implement their own to_string() method.")
