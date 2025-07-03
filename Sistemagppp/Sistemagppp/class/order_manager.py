class OrderManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance.orders = []
        return cls._instance

    def add_order(self, order):
        self.orders.append(order)

    def list_orders(self):
        return self.orders
