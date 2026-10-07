class ItemVenda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.valor_item = produto.preco_unitario

    def calcular_subtotal(self):
        return self.quantidade * self.valor_item


class Venda:
    def __init__(self, data):
        self.data = data
        self.itens = []
        self.__valor_total = 0.0

    def get_valor_total(self):
        return self.__valor_total

    def adicionar_item(self, produto, quant):
        if produto.decrementar_estoque(quant):
            novo_item = ItemVenda(produto, quant)
            self.itens.append(novo_item)
            self.calcular_total()
            return True
        return False

    def remover_item(self, produto):
        for item in self.itens:
            if item.produto == produto:
                produto._Produto__estoque += item.quantidade
                self.itens.remove(item)
                self.calcular_total()
                return True
        return False

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.calcular_subtotal()
        self.__valor_total = total
        return self.__valor_total
