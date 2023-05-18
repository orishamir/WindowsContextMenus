from src.conditions.operators.ioperator import IOperator

AQS_INEQUALITY_OPERATOR = "<>"


class NotEqual(IOperator):
    def __init__(self, to: str | int | float):
        if not isinstance(to, str | int | float):
            raise ValueError("Value must be str/int/float.")

        self.to = to

    def to_aqs_string(self) -> str:
        # Looks like :<>{val}
        if isinstance(self.to, str):
            return f':{AQS_INEQUALITY_OPERATOR}"{self.to}"'
        return f":{AQS_INEQUALITY_OPERATOR}{self.to}"
