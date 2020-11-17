import os

qt_elementos = int(input("\n\n\t\tIndique quantos elementos deseja ter na lista: "))

def del_duplicados(lista):
    nova_lista = []
    lista.sort()
    for i in range(qt_elementos):
        numero = lista[i]
        if nova_lista.count(numero) == 0:
            nova_lista.append(numero)
    return ( nova_lista)        



lista = []
for i in range(qt_elementos):
    valido = False
    while not valido:
        try:
            numero = int(input("\n\n\t\tNumero para adicionar á lista: "))
            lista.append(numero)
        except ValueError:
            print("O valor inserido é inválido. Por favor tente novamente: ")
        else:
            valido = True

programa = del_duplicados(lista)
print(programa)                





