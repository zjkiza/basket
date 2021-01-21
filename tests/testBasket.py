import unittest
from entity.item import Item
from entity.product import Product
from entity.manufacturer import Manufacture
from service.basket import Basket


class BasketTestCase(unittest.TestCase):
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

        self.product_name2 = "Product 2"
        self.product_sku2 = "a002"
        self.product_price2 = 10

        self.product2 = Product(
            name=self.product_name2,
            sku=self.product_sku2,
            price=self.product_price2,
            manufacture=self.manufacture,
        )

    def test_add_item(self):
        basket = Basket()

        item1 = Item(product=self.product1, quantity=1)  # total 1 x 5 = 5
        two_items1 = Item(product=self.product1, quantity=2)  # total 2 x 5 = 10

        # assert basket is empty before real testing
        self.assertEqual(0, basket.count())
        self.assertIsNone(basket.get_item_from_product(self.product1))
        self.assertIsNone(basket.get_item_from_product(self.product2))

        # add 1 product
        basket.add_item(item1)
        self.assertEqual(item1, basket.get_item_from_product(self.product1))
        self.assertEqual(1, basket.get_quantity_for_product(self.product1))
        self.assertEqual(1, basket.count())
        self.assertEqual(5, basket.get_total())

        # same product, 2 more of them added to basket
        basket.add_item(two_items1)
        self.assertEqual(3, basket.get_quantity_for_product(self.product1))
        self.assertEqual(1, basket.count())
        self.assertEqual(15, basket.get_total())

        item2 = Item(product=self.product2, quantity=5)  # total 5 x 10 = 50
        basket.add_item(item2)

        self.assertEqual(2, basket.count())
        self.assertEqual(65, basket.get_total())

    def test_remove_item(self):

        basket = Basket()
        item1 = Item(product=self.product1, quantity=1)  # total  5 x 1 = 5
        item2 = Item(product=self.product2, quantity=3)  # total 10 x 3 = 30
        basket.add_item(item1)
        basket.add_item(item2)

        self.assertEqual(2, basket.count())
        self.assertEqual(35, basket.get_total())

        # remove Product1
        basket.remove_product(self.product1)
        self.assertIsNone(basket.get_item_from_product(self.product1))
        self.assertEqual(1, basket.count())
        self.assertEqual(30, basket.get_total())


if __name__ == "__main__":
    unittest.main()
