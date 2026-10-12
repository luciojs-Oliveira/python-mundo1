# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Qual a largura da parede em metros: "))
altura = float(input("Qual a altura da parede em metros: "))
print("=================================================")
area = largura * altura
tinta = area / 2

# Corrigido de m² para m na largura e altura, e adicionada formatação de 2 casas decimais
print("Largura de {:.2f} m x Altura de {:.2f} m".format(largura, altura))
print("=================================================")
print("A área da parede é de {:.2f} m²".format(area))
print("=================================================")
print("Você precisará de {:.2f} litros de tinta para pintar a parede.".format(tinta))