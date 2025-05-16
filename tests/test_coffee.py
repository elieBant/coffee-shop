import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("ab")
        with self.assertRaises(ValueError):
            Coffee(123)

    def test_num_orders_and_average(self):
        c = Customer("Bob")
        coffee = Coffee("Cappuccino")
        c.create_order(coffee, 4.0)
        c.create_order(coffee, 6.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 5.0)

