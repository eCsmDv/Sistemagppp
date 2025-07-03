import unittest
from classes.order_manager import OrderManager
from classes.order_builder import OrderBuilder
from classes.shipping_strategy import NormalShipping, ExpressShipping, ShippingContext

class TestOrderManager(unittest.TestCase):
    def test_singleton_instance(self):
        m1 = OrderManager()
        m2 = OrderManager()
        self.assertIs(m1, m2)

class TestOrderBuilder(unittest.TestCase):
    def test_build_order(self):
        order = OrderBuilder().add_customer("João").add_product("Notebook").set_shipping("Expresso").build()
        self.assertEqual(order["customer"], "João")
        self.assertIn("Notebook", order["products"])
        self.assertEqual(order["shipping"], "Expresso")

class TestShippingStrategy(unittest.TestCase):
    def test_normal_shipping(self):
        s = ShippingContext(NormalShipping())
        self.assertEqual(s.calculate_shipping(10), 10.0)

    def test_express_shipping(self):
        s = ShippingContext(ExpressShipping())
        self.assertEqual(s.calculate_shipping(10), 20.0)

if __name__ == '__main__':
    unittest.main()
