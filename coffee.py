class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Le nom doit être une chaîne de caractères.")
        if len(name) < 3:
            raise ValueError("Le nom doit faire au moins 3 caractères.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)


