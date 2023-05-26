from src.operators.ioperator import IOperator


class EndsWith(IOperator):
    def __init__(self, ends_with: str):
        if not isinstance(ends_with, str):
            raise TypeError(f"Value must be str. Type is {type(ends_with)}")

        self.ends_with = ends_with

    def to_aqs_string(self) -> str:
        return f":~>{self.ends_with}"
