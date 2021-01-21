from helper.my_type import MyType


class Manufacture:
    def __init__(self):
        self._name = None

    def set_name(self, name: str) -> None:
        MyType.check("manufacturer name", name, str)
        self._name = name

    def get_name(self) -> str:
        return self._name
