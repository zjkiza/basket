import decimal


class MyType:
    @staticmethod
    def check(variable_name, value, exception_type) -> None:
        if not isinstance(value, exception_type):
            raise TypeError(f"Excepted {exception_type} for {variable_name}")

    @staticmethod
    def new_decimal(value: float) -> decimal:
        if isinstance(value, float):
            value = repr(value)
        return decimal.Decimal(value)
