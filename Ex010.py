# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Digite o valor em reais: R$ "))
cotacao = 5.27  # Exemplo de cotação do dólar

conversor = real / cotacao

print("Convertendo R$ {:.2f} reais você terá US$ {:.2f} dólares.".format(real, conversor))