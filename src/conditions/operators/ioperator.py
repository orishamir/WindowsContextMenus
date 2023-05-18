from abc import abstractmethod, ABC


class IOperator(ABC):
    """
    This interface represents an operator for example ==, !=, etc.
    See more:
        https://learn.microsoft.com/en-us/windows/win32/search/-search-3x-advancedquerysyntax#query-operators
    """

    @abstractmethod
    def to_aqs_string(self) -> str:
        """
        Convert this operator to the equivalent Advanced Query Standard (aqs) string
        """

        raise NotImplementedError("Operators should implement their own to_aqs_string() method")
