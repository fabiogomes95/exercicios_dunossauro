#Autor: Fabio Gomes da Silva
#Date: 26/03/2026
"""
Exercício 11: Operações Matemáticas
Enunciado: Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre: 
o produto do dobro do primeiro com metade do segundo; 
a soma do triplo do primeiro com o terceiro; 
o terceiro elevado ao cubo.
Link: https://exercicios.dunossauro.com/01_estrutura_sequencial/#__tabbed_1_11
"""

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int (input("Digite o segundo número inteiro: ")) 
n3 = float (input("Digite o primeiro número real: "))

produto = (n1 * 2) * (n2 / 2)
soma = (n1 * 3) + n3
cubo = n3 ** 3

print(f"o produto do dobro de {n1} com metade de {n2} é: {produto}")
print(f"A soma do tripo de {n1} com {n3} é: {soma} ")
print(f"O cubo de {n3} é: {cubo}")