#Ler a faturação mensal de uma empresa ao longo de 12 meses (janeiro a dezembro) e indicar o mes de maior e menor faturação e a media mensal de faturação

def maior_faturacao(lista_valores):
    maior = max(lista_valores)
    pos = lista_valores.index(maior)
    mes = lista_meses[pos]
    return mes

def menor_faturacao(lista_valores):
    menor = min(lista_valores)
    pos = lista_valores.index(menor)
    mes = lista_meses[pos]
    return mes

lista_meses = []
lista_valores = []
for i in range(12):
    meses = input("\n\n\t\t Insira o mês: ")
    valido = False
    while not valido:
        try:
            valor = int(input("\n\n\t\t Insira o valor: "))
            if valor <0 :
                raise ValueError()
            lista_meses.append(meses)
            lista_valores.append(valor)
        except ValueError:
            print("\n\n\t\t Formato incorreto, tente novamente: ")
        else:
            valido = True   

media = sum(lista_valores) / 12
print("Média: {0}".format(media))

resultado_maior = maior_faturacao(lista_valores)
resultado_menor = menor_faturacao(lista_valores)

print("Mês de maior faturação: {0}".format(resultado_maior))
print("Mês de menor faturação: {0}".format(resultado_menor))