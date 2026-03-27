#Autor: Fabio Gomes da Silva
#Date: 26/03/2026
"""
Exercício 14: João Pescador (Multa por Excesso)
Enunciado: João comprou um computador para controlar seu trabalho. 
Toda vez que ele traz um peso de peixes maior que 50 quilos deve pagar uma multa de R$ 4,00 por quilo excedente. 
Faça um programa que leia a variável peso e calcule o excesso. Gravar a quantidade além do limite e o valor da multa. 
Imprima as mensagens adequadas.
Link: https://exercicios.dunossauro.com/01_estrutura_sequencial/#__tabbed_1_14
"""

peso = float(input("Digite o peso do peixe: "))

valor = max(0, peso - 50) # O max(0, ...) garante que o excesso nunca seja negativo caso o peso seja menor que 50kg (lembrando que ainda não estamos usando if/else ate aqui)
multa = valor * 4 

print(f"O valor excedente foi: {valor} e a multa foi de {multa}")