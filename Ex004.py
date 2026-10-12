# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input("Digte algo: ")
print("O tipo primitivo desse valor é: ", type(a))
print("Só tem espaços ? ", a.isspace())
print("É um número ? ", a.isnumeric())
print("É alfanumerico ?", a.isalnum())
print("Esta em maiusculo ?", a.isupper())
print("Esta em minusculo ?", a.islower())
print("Esta capitalizada ?", a.istitle())






