from classes.order_manager import OrderManager
from classes.order_builder import OrderBuilder
from classes.shipping_strategy import ExpressShipping, ShippingContext
from utils.file_export import FileExport

class PedidoFacade:
    def __init__(self):
        self.manager = OrderManager()

    def criar_pedido(self, cliente, produtos, frete):
        builder = OrderBuilder().add_customer(cliente)
        for p in produtos:
            builder.add_product(p)
        pedido = builder.set_shipping(frete).build()
        self.manager.add_order(pedido)
        return pedido

    def listar_pedidos(self):
        return self.manager.list_orders()

    def gerar_relatorio_pdf(self):
        pedidos = self.manager.list_orders()
        relatorio = "Relatório de Pedidos:\n\n"
        for p in pedidos:
            relatorio += str(p) + "\n"
        FileExport.save_to_file("relatorio.txt", relatorio)
