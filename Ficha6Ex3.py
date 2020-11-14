#Ler a ontuação de 10 participantes (0 a 20) , devolver uma lista com apenas as pontuações positivas

def positive(lista):
    lista_positivas = []
    for i in range(len(lista)):
        if lista[i] >= 10:
            lista_positivas.append(lista[i])
    return lista_positivas  
    
lista = []
for i in range(10):
    valido = False
    while not valido:
        try:
            number= int(input("Pontuação: "))   
            if number <0 or number >20:
                raise ValueError()
            lista.append(number)
        except ValueError:
            print("Valor invalido, tente novamente")
        else:
            valido = True          

lista_positivas = positive(lista)

print("Positivas: {0}".format(lista_positivas))




