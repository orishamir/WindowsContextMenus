from src.conditions.base_class.condition_base_class import ConditionBase
from src.conditions.operators import IOperator, Equal

PROPERTY_NAME = "System.FileExtension"


class ExtensionType(ConditionBase):
    """
    This condition checks the value of the extension of the file.
    """

    def __init__(self, ext: str | IOperator):
        if isinstance(ext, str):
            ext = Equal(ext)

        if not isinstance(ext, IOperator):
            raise TypeError(f"Extension should either be a string or an operator. Not {type(ext)}")

        self.ext = ext

    def to_aqs_string(self) -> str:
        """
        Convert condition to its AQS representation.
        """

        return f"({PROPERTY_NAME}{self.ext.to_aqs_string()})"
