from src.comparers.icomparer import IComparer


class NotEqual(IComparer):
    def __init__(self, to: str | int | float):
        if not isinstance(to, str | int | float):
            raise TypeError(f"Value must be str/int/float. Type is {type(to)}")

        self.to = to

    def to_aqs_string(self) -> str:
        # Looks like :<>{val}
        if isinstance(self.to, str):
            return f':<>"{self.to}"'
        return f":<>{self.to}"
