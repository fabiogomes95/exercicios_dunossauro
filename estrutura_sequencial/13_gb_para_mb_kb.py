#Autor: Fabio Gomes da Silva
#Date: 26/03/2026
"""
Exercício 13: Gigabytes para Mega e Kilobytes
Enunciado: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:
 Para Megabytes: Gigabytes * 1024. Para Kilobytes: Gigabytes * 1024 * 1024.
Link: https://exercicios.dunossauro.com/01_estrutura_sequencial/#__tabbed_1_13
"""

giga = float(input("Digite o tamanho do arquivo em Gigabytes: "))
mega = giga * 1024
kilo = mega * 1024
print(f"{giga} Gigabytes é {mega} MegaBytes e {kilo} Kilobytes")