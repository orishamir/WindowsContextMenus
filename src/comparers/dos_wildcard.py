from src.comparers.icomparer import IComparer


class DosWildcard(IComparer):
    def __init__(self, string: str):
        if not isinstance(string, str):
            raise TypeError(f"Value must be str. Type is {type(string)}")

        self.string = string

    def to_aqs_string(self) -> str:
        return f"~{self.string}"
