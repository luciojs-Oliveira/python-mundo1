# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

salario = float(input("Informe o seu salário: R$ "))

reajuste = salario + (salario * 15 / 100)

print("O salário informado foi R$ {:.2f}".format(salario))
print("O novo salário com 15% de aumento será R$ {:.2f}".format(reajuste))