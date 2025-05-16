# Coffee Shop

This project models a simple coffee shop system with customers, coffees, and orders. It demonstrates object-oriented programming concepts such as classes, relationships, and data validation in Python.

## Installation

No special installation is required. The project uses standard Python 3 and the built-in `unittest` framework for testing.

## Usage

Here is a basic example demonstrating how to create customers, coffees, and orders:

```python
from customer import Customer
from coffee import Coffee

customer = Customer("Elie")
coffee = Coffee("Latte")
order = customer.create_order(coffee, 3.5)

print(f"Customer: {customer.name}")
print("Coffees ordered:", [c.name for c in customer.coffees()])
print("Order price:", order.price)
```

## Main Classes

### Customer

- Represents a customer with a validated name (1 to 15 characters).
- Tracks orders made by the customer.
- Methods:
  - `orders()`: Returns all orders by the customer.
  - `coffees()`: Returns unique coffees ordered.
  - `create_order(coffee, price)`: Creates a new order for a coffee at a given price.

### Coffee

- Represents a coffee with a validated name (at least 3 characters).
- Tracks orders for this coffee.
- Methods:
  - `orders()`: Returns all orders for this coffee.
  - `customers()`: Returns unique customers who ordered this coffee.
  - `num_orders()`: Returns the number of orders.
  - `average_price()`: Returns the average price of all orders.

### Order

- Represents an order linking a customer and a coffee with a price.
- Validates that customer and coffee are instances of their respective classes.
- Validates price is between 1.0 and 10.0.
- Properties:
  - `customer`
  - `coffee`
  - `price`

## Testing

The project includes unit tests using Python's built-in `unittest` framework. To run the tests, execute:

```bash
python -m unittest discover tests
```

This will run all tests in the `tests` directory.

## License

This project is provided as-is without any specific license.
