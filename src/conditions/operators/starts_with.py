from src.conditions.operators.ioperator import IOperator


class StartsWith(IOperator):
    def __init__(self, starts_with: str):
        if not isinstance(starts_with, str):
            raise TypeError(f"Value must be str. Type is {type(starts_with)}")

        self.starts_with = starts_with

    def to_aqs_string(self) -> str:
        return f":~<{self.starts_with}"
