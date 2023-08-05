from src.comparers.icomparer import IComparer


class Contains(IComparer):
    def __init__(self, substr: str):
        if not isinstance(substr, str):
            raise TypeError(f"Value must be str. Type is {type(substr)}")

        self.substr = substr

    def to_aqs_string(self) -> str:
        return f"~={self.substr}"
