#Ler a ontuação de 10 participantes (0 a 20) , devolver uma lista com nomes e respetivas pontuações

def positive(lista, lista_nomes):
    lista_positivas = []
    l_nomes = []
    for i in range(len(lista)):
        if lista[i] >= 10:
            lista_positivas.append(lista[i])
            l_nomes.append(lista_nomes[i])
    return lista_positivas, l_nomes
    
lista = []
lista_nomes = []
for i in range(10):
    name = input("Nome: ") 
    valido = False
    while not valido:
        try:
            number= int(input("Pontuação: ")) 
            if number <0 or number >20:
                raise ValueError()
            lista.append(number)
            lista_nomes.append(name)
        except ValueError:
            print("Valor invalido, tente novamente")
        else:
            valido = True          

l_nomes = positive(lista, lista_nomes)


print("Positivas: {0}".format(l_nomes))
