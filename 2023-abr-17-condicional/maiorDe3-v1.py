'''
Este programa pergunta três números e informa o maior deles.
Por Galileu Batista - Abr 2023
IFRN/CNAT
'''

x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))
z = int(input("Informe o terceiro número: "))

if x < y:
    if z < y:
        print ("O maior número é ", y)
    else:
        print ("O maior número é ", z)
else:
    if z < x:
        print ("O maior número é ", x)
    else:
        print ("O maior número é ", z)

print ("Bye!")