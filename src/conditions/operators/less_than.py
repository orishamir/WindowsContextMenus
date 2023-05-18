from src.conditions.operators.ioperator import IOperator


class LessThan(IOperator):
    def __init__(self, than: str | int | float):
        if not isinstance(than, str | int | float):
            raise ValueError("Value must be str/int/float.")

        self.than = than

    def to_aqs_string(self) -> str:
        return f":<{self.than}"
