

def ordenar(lista_valor):
    lista_valor.sort()
    lista_valor.reverse()
    return lista_valor



lista_valor = []
for i in range(12):
    valido = False
    while not valido:
        try:
            numero = int(input("\n\n\t\tValor: "))
            if numero < 0:
                raise ValueError()
            lista_valor.append(numero)
        except ValueError:
            print("\n\n\t\tFormato incorreto, por favor tente novamente: ")
        else:
            valido = True    

lista_ordenada = ordenar(lista_valor)
print("\n\n\t\t{0}".format(lista_ordenada))