class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer  # import local pour éviter cercle
        from coffee import Coffee      # import local aussi

        if not isinstance(customer, Customer):
            raise TypeError("customer doit être une instance de Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee doit être une instance de Coffee")
        if not isinstance(price, (float, int)):
            raise ValueError("price doit être un nombre (float ou int)")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("price doit être entre 1.0 et 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price


