from customer import Customer
from coffee import Coffee

def main():
    customer = Customer("Elie")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 3.5)

    print(f"Customer: {customer.name}")
    print("Coffees ordered:", [c.name for c in customer.coffees()])
    print("Order price:", order.price)

if __name__ == "__main__":
    main()



