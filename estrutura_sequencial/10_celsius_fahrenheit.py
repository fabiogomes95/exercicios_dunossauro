#Autor: Fabio Gomes da Silva
#Date: 26/03/2026
"""
Exercício 10: Celsius para Fahrenheit
Enunciado: Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. Fórmula: F = (C * 9/5) + 32.
Link: https://exercicios.dunossauro.com/01_estrutura_sequencial/#__tabbed_1_10
"""

celcius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"{celcius:.1f}°C é {fahrenheit:.1f}°F")