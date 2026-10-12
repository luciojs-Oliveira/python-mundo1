# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

valorProduto = float(input("Digite o valor do produto: R$ "))

desconto = valorProduto - (valorProduto * 5 / 100)

print("O produto custa R$ {:.2f}, com desconto de 5% custará R$ {:.2f}".format(valorProduto, desconto))