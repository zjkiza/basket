import unittest
from entity.category import Category
from entity.product import Product
from entity.manufacturer import Manufacture


class CategoryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.category = Category("Category 1")

        self.manufacturer = Manufacture()
        self.manufacturer.set_name("Manufacturer No1")

    def test_add_product(self):
        # must by empty
        self.assertEqual(0, len(self.category.products))

        product1 = Product(
            sku="a001", name="Product 1", price=10, manufacture=self.manufacturer
        )
        product2 = Product(
            sku="a002", name="Product 2", price=9, manufacture=self.manufacturer
        )

        # add product1
        self.category.add_product(product1)

        self.assertTrue(self.category.has_product(product1))
        self.assertEqual(1, len(self.category.products))
        self.assertFalse(self.category.has_product(product2))

        self.assertTrue(product1.has_category(self.category))
        self.assertEqual(1, len(product1.categories))

        # add product2

        self.category.add_product(product2)
        self.assertTrue(self.category.has_product(product2))
        self.assertEqual(2, len(self.category.products))

        self.assertTrue(product2.has_category(self.category))
        self.assertEqual(1, len(product2.categories))

    def test_remove_product(self):
        # must by empty
        self.assertEqual(0, len(self.category.products))

        product1 = Product(
            sku="a001", name="Product 1", price=10, manufacture=self.manufacturer
        )
        product2 = Product(
            sku="a002", name="Product 2", price=9, manufacture=self.manufacturer
        )

        self.category.add_product(product1)
        self.category.add_product(product2)
        self.assertEqual(2, len(self.category.products))

        # remove product2
        self.category.remove_product(product2)
        self.assertFalse(self.category.has_product(product2))
        self.assertFalse(product2.has_category(self.category))

        # assert that product1 is not affected
        self.assertTrue(self.category.has_product(product1))
        self.assertTrue(product1.has_category(self.category))
