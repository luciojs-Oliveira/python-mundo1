# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e o seu antecessor.


num = int(input("Digite um número : "))

antecessor = num -1
sucessor = num + 1

print("O número digitado foi: {} O seu antecessor é : {}, e o seu sucessor é : {}".format(num, antecessor, sucessor))
