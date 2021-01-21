from .product import Product


class Category:
    def __init__(self, category):
        self._category = category
        self._products = []

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def products(self) -> list:
        return self._products

    def add_product(self, product: Product) -> None:
        if not self.has_product(product):
            self._products.append(product)
            product.add_category(self)

    def has_product(self, product: Product) -> bool:
        return product in self._products

    def remove_product(self, product: Product) -> None:
        if self.has_product(product):
            self._products.remove(product)
            product.remove_category(self)
