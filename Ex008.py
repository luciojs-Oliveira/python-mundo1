# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Digite um valor: "))

conversor = medida * 100

print("{} metro(s) convertido(s) são : {} centímetros" .format(medida, conversor))
