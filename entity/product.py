from .manufacturer import Manufacture


class Product:
    __slots__ = ("_manufacture", "_price", "_name", "_sku", "_category")

    def __init__(self, sku: str, name: str, price: float, manufacture: Manufacture):
        self._manufacture = manufacture
        self._price = price
        self._name = name
        self._sku = sku
        self._category = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        self._price = value

    @property
    def sku(self) -> str:
        return self._sku

    @sku.setter
    def sku(self, value) -> None:
        self._sku = value

    @property
    def manufacture(self) -> Manufacture:
        return self._manufacture

    @manufacture.setter
    def manufacture(self, value) -> None:
        self._manufacture = value

    @property
    def categories(self) -> list:
        return self._category

    def add_category(self, category) -> None:
        if not self.has_category(category):
            self._category.append(category)
            category.add_product(self)

    def has_category(self, category) -> bool:
        return category in self._category

    def remove_category(self, category):
        if self.has_category(category):
            self._category.remove(category)
            category.remove_product(self)
