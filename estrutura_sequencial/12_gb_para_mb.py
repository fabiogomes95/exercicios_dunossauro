#Autor: Fabio Gomes da Silva
#Date: 26/03/2026
"""
Exercício 12: Gigabytes para Megabytes
Enunciado: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula: 
Megabytes = Gigabytes * 1024.
Link: https://exercicios.dunossauro.com/01_estrutura_sequencial/#__tabbed_1_12
"""
giga = float(input("Digite o tamanho do arquivo em Gigabytes: "))
mega = giga * 1024
print(f"{giga} Gigabytes é {mega} MegaBytes")