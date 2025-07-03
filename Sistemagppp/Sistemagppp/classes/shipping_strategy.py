class ShippingStrategy:
    def calculate(self, distance):
        pass

class NormalShipping(ShippingStrategy):
    def calculate(self, distance):
        return distance * 1.0

class ExpressShipping(ShippingStrategy):
    def calculate(self, distance):
        return distance * 2.0

class InternationalShipping(ShippingStrategy):
    def calculate(self, distance):
        return distance * 3.0

class ShippingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_shipping(self, distance):
        return self.strategy.calculate(distance)
