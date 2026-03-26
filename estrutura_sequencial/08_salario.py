#Autor: Fabio Gomes da Silva
#Date: 26/03/2026
"""
Exercício 08: Salário por Hora
Enunciado: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
Link: https://exercicios.dunossauro.com/01_estrutura_sequencial/#__tabbed_1_8
"""

salario_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalha mensal? "))

total_salario = salario_hora * horas_trabalhadas
print(f"Seu salario mensal será R$ {total_salario:.2f}")