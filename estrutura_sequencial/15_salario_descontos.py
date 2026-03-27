#Autor: Fabio Gomes da Silva
#Date: 26/03/2026
"""
Exercício 15: Salário Líquido e Descontos
Enunciado: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no mês, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato. 
Calcule o salário bruto, descontos e salário líquido.
Link: https://exercicios.dunossauro.com/01_estrutura_sequencial/#__tabbed_1_15
"""

salario_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalha mensal? "))

salario_bruto = salario_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindc = salario_bruto * 0.05
liquido = salario_bruto - ir - inss - sindc

# Formatação de strings (f-strings):
# :.<20 -> Alinha o texto à esquerda em um bloco de 20 caracteres, preenchendo com pontos.
# :>8.2f -> Alinha o valor à direita em um bloco de 8 caracteres com 2 casas decimais.

print(f"{'+ Salário Bruto':.<20}: R$ {salario_bruto:>8.2f}")
print(f"{'- IR (11%)':.<20}: R$ {ir:>8.2f}")
print(f"{'- INSS (8%)':.<20}: R$ {inss:>8.2f}")
print(f"{'- Sindicato (5%)':.<20}: R$ {sindc:>8.2f}")
print(f"{'= Salario Liquido':.<20}: R$ {liquido:>8.2f}")

