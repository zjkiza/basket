from .product import Product


class Item:
    __slots__ = ("_quantity", "_product")

    def __init__(self, product: Product, quantity: int):
        self._quantity = quantity
        self._product = product

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity

    def add_quantity(self, value):
        self._quantity += value

    def total_price(self):
        return self.quantity * self.product.price
