#Chave do euromilhoes de forma aleatoria

restart = "S"
while restart == "S":

    import random

    lista1 =[]
    lista2 =[]
    for i in range(5):
        numero = random.randint(1,50)
        if numero not in lista1:
            lista1.append(numero)

    for i in range(2):
        estrela = random.randint(1,12)
        if estrela not in lista2:
            lista2.append(estrela)
        
    lista1.append(lista2)
    print("\n\n\t\t",lista1)
    restart = input("\n\n\t\t Deseja jogar novamente? (S/N) : ")
print("Volte Sempre")