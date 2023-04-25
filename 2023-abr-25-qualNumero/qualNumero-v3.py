'''
Este programa escolhe um número e dá três chances para o usuário acertar.
Por Galileu Batista - Abr 2023
IFRN/CNAT
'''

import random

print ("Seu desafio é descobrir o número que eu possuo ... ")
min = 1
max = 100
secreto = random.randint(min, max)
acertou = False

if acertou == False:
    escolha = int (input ("Escolha entre "+str(min)+" e "+str(max)+": "))
    if escolha == secreto:
        acertou = True
    elif escolha > secreto:
        max = escolha
    else:
        min = escolha

if acertou == False:
    escolha = int (input ("Escolha entre "+str(min)+" e "+str(max)+": "))
    if escolha == secreto:
        acertou = True
    elif escolha > secreto:
        max = escolha
    else:
        min = escolha

if acertou == False:
    escolha = int (input ("Escolha entre "+str(min)+" e "+str(max)+": "))
    if escolha == secreto:
        acertou = True
    elif escolha > secreto:
        max = escolha
    else:
        min = escolha


if acertou == True:
    print ("Voce acertou o número. Era ", secreto)
else:
    print ("Lamento. Número de tentativas excedidas. Era ", secreto)
