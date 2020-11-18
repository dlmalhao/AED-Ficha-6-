#Juntar duas listas ordenadas e mantelas ordenadas

n = int(input("\n\n\t\tIndique a quantidade de elementos da lista 1: "))
n2 = int(input("\n\n\t\tIndique a quantidade de elementos da lista 2: "))

lista1 = []
lista2 = []
for i in range(n):
    numero = int(input("\n\n\t\tIndique um numero para a lista 1: "))
    lista1.append(numero)
    pos = lista1[i]

    
for i in range(n2):
    numero2 = int(input("\n\n\t\tIndique um numero para a lista 2: "))
    lista2.append(numero2)
    pos2 = lista2[i]

nova_lista = lista1 + lista2
nova_lista.sort()
print(nova_lista)


