class OrderBuilder:
    def __init__(self):
        self.order = {}

    def add_customer(self, name):
        self.order["customer"] = name
        return self

    def add_product(self, product):
        if "products" not in self.order:
            self.order["products"] = []
        self.order["products"].append(product)
        return self

    def set_shipping(self, shipping_type):
        self.order["shipping"] = shipping_type
        return self

    def build(self):
        return self.order
