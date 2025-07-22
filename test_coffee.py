import unittest
from main import Coffee, Order

class TestCoffeeOrder(unittest.TestCase):
    def test_add_invalid_price(self):
        order=Order()
        bad_coffee=Coffee("Flat white", "3 dollars")
        order.add_item(bad_coffee)
        with self.assertRaises(TypeError):
            order.total()
            
    def test_add_item(self):
        order=Order()
        coffee=Coffee("TestCoffee", 5.0)
        order.add_item(coffee)
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.items[0].name, "TestCoffee")

    def test_total(self):
        order=Order()
        order.add_item(Coffee("One", 2.0))
        order.add_item(Coffee("Two", 3.0))
        self.assertEqual(order.total(), 5.0)

if __name__=='__main__':
    unittest.main()