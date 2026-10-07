class Produto:
    def __init__(self, descricao, preco_unitario, estoque):
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.__estoque = estoque 

    def get_estoque(self):
        return self.__estoque

    def decrementar_estoque(self, quant):
        if quant > 0 and self.__estoque >= quant:
            self.__estoque -= quant
            return True
        return False
