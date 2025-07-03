import tkinter as tk
from tkinter import simpledialog, messagebox
from classes.facade import PedidoFacade

class SistemaGPPPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema GPPP - Gerenciamento de Pedidos")
        self.root.geometry("600x600")

        self.facade = PedidoFacade()
        self.setup_interface()

    def setup_interface(self):
        tk.Label(self.root, text="Gerenciamento de Pedidos", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Novo Pedido", width=20, command=self.criar_pedido).pack(pady=5)
        tk.Button(self.root, text="Listar Pedidos", width=20, command=self.listar_pedidos).pack(pady=5)
        tk.Button(self.root, text="Gerar Relatório PDF", width=20, command=self.gerar_relatorio).pack(pady=5)
        tk.Button(self.root, text="Sair", width=20, command=self.root.quit).pack(pady=20)

    def criar_pedido(self):
        cliente = simpledialog.askstring("Novo Pedido", "Nome do Cliente:")
        if not cliente:
            return
        produtos = []
        while True:
            produto = simpledialog.askstring("Adicionar Produto", "Nome do Produto (ou clique Cancelar para finalizar):")
            if not produto:
                break
            produtos.append(produto)
        if not produtos:
            messagebox.showinfo("Erro", "Adicione ao menos um produto.")
            return
        frete = simpledialog.askstring("Frete", "Tipo de Frete (Normal / Expresso / Internacional):", initialvalue="Normal")
        self.facade.criar_pedido(cliente, produtos, frete)
        messagebox.showinfo("Pedido", "Pedido criado com sucesso!")

    def listar_pedidos(self):
        pedidos = self.facade.listar_pedidos()
        if not pedidos:
            messagebox.showinfo("Pedidos", "Nenhum pedido registrado.")
        else:
            lista = "\n".join(str(p) for p in pedidos)
            messagebox.showinfo("Pedidos", lista)

    def gerar_relatorio(self):
        self.facade.gerar_relatorio_pdf()
        messagebox.showinfo("Relatório", "Relatório gerado como relatorio.txt")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaGPPPApp(root)
    root.mainloop()
