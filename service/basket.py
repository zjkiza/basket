from entity.item import Item
from entity.product import Product
from typing import Optional


class Basket:
    def __init__(self):
        self._items = []

    def add_item(self, item: Item) -> None:
        exist_item = self.get_item_from_product(item.product)
        # if exist_item:
        #     exist_item.add_quantity(item.quantity)
        #     return
        #
        # self._items.append(item)
        exist_item.add_quantity(item.quantity) if exist_item else self._items.append(
            item
        )

    def remove_product(self, product: Product) -> bool:
        exist_item = self.get_item_from_product(product)
        if exist_item:
            self._items.remove(exist_item)
            return True

        return False

    def get_quantity_for_product(self, product: Product) -> int:
        exist_item = self.get_item_from_product(product)
        # if exist_item:
        #     return exist_item.quantity
        #
        # return 0
        return exist_item.quantity if exist_item else 0

    def count(self) -> int:
        return len(self._items)

    def get_total(self) -> float:
        return sum([item.total_price() for item in self._items])

    def get_item_from_product(self, product: Product) -> Optional[Item]:
        for item in self._items:
            if item.product == product:
                return item

        return None

    def display(self):
        for item in self._items:
            print(
                item.product.sku,
                item.product.manufacture.get_name(),
                item.product.name,
                item.product.price,
                item.quantity,
            )
