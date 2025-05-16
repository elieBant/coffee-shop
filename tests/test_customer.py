import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("a" * 16)
        with self.assertRaises(ValueError):
            Customer(123)

    def test_orders_and_coffees(self):
        c = Customer("Alice")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        c.create_order(coffee1, 5.0)
        c.create_order(coffee2, 6.0)
        c.create_order(coffee1, 4.5)

        self.assertEqual(len(c.orders()), 3)
        self.assertEqual(set(c.coffees()), {coffee1, coffee2})

