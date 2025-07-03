class PayPal:
    def enviar_pagamento(self, valor):
        print(f"Pagamento de R${valor} enviado via PayPal.")

class PagamentoAdapter:
    def __init__(self, metodo_pagamento):
        self.metodo = metodo_pagamento

    def pagar(self, valor):
        self.metodo.enviar_pagamento(valor)
