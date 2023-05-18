from src.conditions.operators.ioperator import IOperator


class Equal(IOperator):
    def __init__(self, to: str | int | float):
        if not isinstance(to, str | int | float):
            raise ValueError("Value must be str/int/float.")

        self.to = to

    def to_aqs_string(self) -> str:
        if isinstance(self.to, str):
            return f':="{self.to}"'
        return f":={self.to}"
