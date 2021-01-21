import unittest
from entity.item import Item
from entity.product import Product
from entity.manufacturer import Manufacture


class ItemTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.manufacture = Manufacture()
        self.manufacture_name = "Lol"
        self.manufacture.set_name(self.manufacture_name)

        self.product_name1 = "Product 1"
        self.product_sku1 = "a001"
        self.product_price1 = 5

        self.product1 = Product(
            name=self.product_name1,
            sku=self.product_sku1,
            price=self.product_price1,
            manufacture=self.manufacture,
        )

        self.quantity = 10
        self.item = Item(product=self.product1, quantity=self.quantity)

    def test_getter(self):
        self.item = Item(product=self.product1, quantity=10)
        self.assertEqual(self.product1, self.item.product)
        self.assertEqual(self.quantity, self.item.quantity)

    def test_total_price(self):
        self.assertEqual(50, self.item.total_price())

    def test_add_quantity(self):
        self.item.add_quantity(5)
        self.assertEqual(15, self.item.quantity)


if __name__ == "__main__":
    unittest.main()
