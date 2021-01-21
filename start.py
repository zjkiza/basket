from entity.manufacturer import Manufacture
from entity.product import Product
from entity.item import Item
from service.basket import Basket

manufacture = Manufacture()
manufacture.set_name('HP')

product1 = Product(sku='a001', name='Product 1', price=5, manufacture=manufacture)
product2 = Product(sku='a002', name='Product 2', price=4, manufacture=manufacture)
product3 = Product(sku='a003', name='Product 3', price=3, manufacture=manufacture)

item1 = Item(product1, 1)
item2 = Item(product2, 2)

print('Add products in basket')

basket = Basket()
basket.add_item(item1)
basket.add_item(item2)

print('Display products from basket')

basket.display()
print('Display count of products in basket')
print(basket.count())
print('Display total values in basket')
print(basket.get_total())

print('-' * 50)
print('Add exist item on basket - product 1 ')
basket.add_item(item1)
basket.display()
print(basket.count())
print(basket.get_total())

print('-' * 50)
print('Get quantity on product 1')
print(basket.get_quantity_for_product(product1))
print('Get quantity on product 3 - not exist')
print(basket.get_quantity_for_product(product3))

print('-' * 50)
print('Add product 3')
item3 = Item(product3, 1)
basket.add_item(item3)
basket.display()
print('Remove product 2')
basket.remove_product(product2)
basket.display()
