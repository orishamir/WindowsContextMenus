from src.operators.ioperator import IOperator


class GreaterThanEqual(IOperator):
    def __init__(self, than: str | int | float):
        if not isinstance(than, str | int | float):
            raise TypeError(f"Value must be str/int/float. Type is {type(than)}")

        self.than = than

    def to_aqs_string(self) -> str:
        return f":>={self.than}"
