from operators.ioperator import IOperator


class Contains(IOperator):
    def __init__(self, substr: str):
        if not isinstance(substr, str):
            raise TypeError(f"Value must be str. Type is {type(substr)}")

        self.substr = substr

    def to_aqs_string(self) -> str:
        return f"~={self.substr}"
