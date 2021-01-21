from entity.product import Product
from entity.manufacturer import Manufacture
import unittest


class ProductTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.manufacture = Manufacture()
        self.manufacture_name = 'Lol'
        self.manufacture.set_name(self.manufacture_name)

        self.product_name = 'Product 1'
        self.product_sku = 'a001'
        self.product_price = 5

        self.product = Product(
            name=self.product_name,
            sku=self.product_sku,
            price=self.product_price,
            manufacture=self.manufacture
        )

    def test_check_data(self):
        self.assertEqual(self.product_name, self.product.name)
        self.assertEqual(self.product_sku, self.product.sku)
        self.assertEqual(self.product_price, self.product.price)
        self.assertEqual(self.manufacture, self.product.manufacture)


if __name__ == '__main__':
    unittest.main()
