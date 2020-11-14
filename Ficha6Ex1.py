#Ler 10 num e indicar quantos estão acima da media

def acima_media(lista):
    media = sum(lista) / len(lista)
    cont = 0
    for i in range(len(lista)):
        if lista[i] > media:
            cont += 1
    return cont        

lista = []
for i in range(10):
    numero = int(input("Indique um numero: "))
    lista.append(numero)
cont = acima_media(lista)
print("Existem {0} numeros acima da media nesta lista".format(cont))