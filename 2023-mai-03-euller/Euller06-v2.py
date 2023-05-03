'''
Este programa resolve o problema 06 do Projeto Euller.
https://projecteuler.net/problem=6
Por Galileu Batista - Mai 2023
IFRN/CNAT
'''

soma = 0
somaQuadrados = 0
x = 1

while x < 1000:
    soma =  soma + x
    somaQuadrados =  somaQuadrados + x*x
    x = x + 1
quadradoSoma = soma * soma


print ("A diferenca entre o quadrado da soma e a soma dos quadrados ",
       "dos numeros  menores do que 1000 é:", quadradoSoma - somaQuadrados)