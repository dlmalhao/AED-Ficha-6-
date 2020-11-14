#Ler a faturação mensal de uma empresa ao longo de 12 meses (janeiro a dezembro) e indicar o mes de maior e menor faturação e a media mensal de faturação

def maior_faturacao(lista_meses, lista_valores):
    lista_maior_mes = []
    lista_maior_valor = []
    for i in range (len(lista_valores)):
        lista_maior_valor.append(max(lista_valores))
        lista_maior_mes.append(lista_meses[i])
    return lista_maior_mes, lista_maior_valor

def menor_faturacao(lista_meses, lista_valores):
    lista_menor_mes = []
    lista_menor_valor = []
    for i in range (len(lista_valores)):
        lista_menor_valor.append(min(lista_valores))
        lista_menor_mes.append(lista_meses[i])
    return lista_menor_mes, lista_menor_valor


lista_meses = []
lista_valores = []
for i in range(12):
    meses = input("\n\n\t\t Insira o mês: ")
    valido = False
    while not valido:
        try:
            valor = int(input("\n\n\t\t Insira o valor: "))
            if valor <0 :
                raise ValueError
            lista_meses.append(meses)
            lista_valores.append(valor)
        except ValueError:
            print("\n\n\t\t Formato incorreto, tente novamente: ")
        else:
            valido = True   

media = sum(lista_valores) / 12

lista_maior_mes = maior_faturacao(lista_meses, lista_valores)
lista_menor_mes = menor_faturacao(lista_meses, lista_valores)
print("Mês de maior faturação: {0}".format(lista_maior_mes))

print("Mês de menor faturação: {0}".format(lista_menor_mes))

print("Média: {0}".format(media))


    
    


    

    