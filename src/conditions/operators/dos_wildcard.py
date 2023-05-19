from src.conditions.operators.ioperator import IOperator


class DosWildcard(IOperator):
    def __init__(self, string: str):
        if not isinstance(string, str):
            raise ValueError(f"Value must be str. Type is {type(string)}")

        self.string = string

    def to_aqs_string(self) -> str:
        return f"~{self.string}"