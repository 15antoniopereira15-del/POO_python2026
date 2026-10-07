from produto import Produto
from venda import Venda

p1 = Produto("Caderno", 15.00, 10)
p2 = Produto("Caneta", 2.50, 20)

print(f"Produto 1: {p1.descricao} | Preço: R$ {p1.preco_unitario} | Estoque: {p1.get_estoque()}")
print(f"Produto 2: {p2.descricao} | Preço: R$ {p2.preco_unitario} | Estoque: {p2.get_estoque()}")

print("\n--- Realizando Venda ---")
minha_venda = Venda("02/10/2026")

if minha_venda.adicionar_item(p1, 2):
    print("Adicionado 2 Cadernos com sucesso!")

if minha_venda.adicionar_item(p2, 4):
    print("Adicionado 4 Canetas com sucesso!")

print(f"\nValor Total da Venda: R$ {minha_venda.get_valor_total():.2f}")
print(f"Estoque atualizado de Cadernos: {p1.get_estoque()}")
print(f"Estoque atualizado de Canetas: {p2.get_estoque()}")
