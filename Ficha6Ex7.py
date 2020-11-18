

import os

def ordenar(lista_valor):
    lista_copy = lista_valor.copy()
    lista_copy.sort()              #Duvidas em como ordenar os meses na funçáo
    lista_copy.reverse()
    for i in range(12):
        pos = lista_valor.index(lista_copy[i])
        print(mes[pos],"\t" ,lista_copy[i])
        lista_valor[pos] = -1


mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
lista_valor = []
for i in range(12):
    valido = False
    while not valido:
        try:
            valor = int(input("\n\n\t\tValor no mes de {0}: ".format(mes[i])))
            if valor < 0:
                raise ValueError()
            lista_valor.append(valor)
        except ValueError:
            print("\n\n\t\tFormato incorreto, por favor tente novamente: ")
        else:
            valido = True    

ordenar(lista_valor)
