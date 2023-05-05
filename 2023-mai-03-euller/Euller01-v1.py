'''
Este programa resolve o problema 01 do Projeto Euller.
https://projecteuler.net/problem=1
Por Galileu Batista - Mai 2023
IFRN/CNAT
'''

soma = 0
x = 1

while x < 1000:
    if (x % 3 == 0) or (x % 5 == 0):
        soma = soma + x
    x = x + 1

print ("A soma dos múltiplos de 3 ou 5, menores do que 1000 é:", soma)