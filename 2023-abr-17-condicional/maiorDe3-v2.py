'''
Este programa pergunta três números e informa o maior deles
Por Galileu Batista - Abr 2023
IFRN/CNAT
'''

x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))
z = int(input("Informe o terceiro número: "))

maior = x
if y > maior:
    maior = y

if z > maior:
    maior = z

print ("O maior número é ", maior)
print ("Bye!")