#Programa que le uma lista e que indica em que posicao esta um certo numero dado pelo utilizador

def posicao(pesquisa):
    pos = lista.index(pesquisa)
    return pos


lista = []
for i in range(10):
    valido = False
    while not valido:
        try:
            numero = int(input("Digite o seu numero: "))
            lista.append(numero)
        except ValueError:
            print("O valor inserido é inválido, tente novamente: ")
        else:
            valido = True        
pesquisa = int(input("Digite o numero que deseja procurar: "))  

pos = posicao(pesquisa)

if pos == -1:
    print("O numero {0} não existe na lista".format(pesquisa))
else:
    print("O numero {0} existe na posição {1} da lista".format(pesquisa,pos+1))