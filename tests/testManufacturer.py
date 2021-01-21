import unittest
from entity.manufacturer import Manufacture


class ManufactureTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.manufacture = Manufacture()
        self.name = "Lol"

    def test_name(self):
        self.manufacture.set_name(self.name)
        self.assertEqual(self.name, self.manufacture.get_name())

    def test_name_type_exception(self):

        # solution 1
        with self.assertRaises(TypeError):
            self.manufacture.set_name(123)

        # solution 2
        self.assertRaises(TypeError, self.manufacture.set_name, 123)


if __name__ == "__main__":
    unittest.main()
