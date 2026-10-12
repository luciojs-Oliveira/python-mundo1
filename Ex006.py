# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz

num = float(input("Informe um número: "))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print("O número informado foi : {}".format(num))
print("O seu dobro é : {}".format(dobro))
print("O seu triplo é : {}".format(triplo))
print("E a sua raiz quadrada é: {:.2f}".format(raiz))