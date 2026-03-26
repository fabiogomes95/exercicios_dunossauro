#Autor: Fabio Gomes da Silva
#Date: 26/03/2026
"""
Exercício 09: Fahrenheit para Celsius
Enunciado: Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. Fórmula: C = 5 * ((F-32) / 9).
Link: https://exercicios.dunossauro.com/01_estrutura_sequencial/#__tabbed_1_9
"""


fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celcius = 5 * ((fahrenheit - 32) / 9)
print(f"{fahrenheit:.1f}°F é {celcius:.1f}°C") 