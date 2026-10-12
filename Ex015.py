# Exercício Python 15: Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por KM rodado.

quilometros = float(input("Quantos quilômetros você percorreu? "))
dias = int(input("Quantos dias você alugou o carro? "))

# Calculando o custo por km e por dia
precoQuilometro = quilometros * 0.15
precodia = dias * 60

# Calculando o total geral
total = precoQuilometro + precodia

print("Você rodou {:.1f} km e alugou por {} dias.".format(quilometros, dias))
print("O total a ser pago é de R$ {:.2f}".format(total))