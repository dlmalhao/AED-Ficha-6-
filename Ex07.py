# Versão que lista a pluviosidade por ordem decrescente, e os respetivos meses

meses = ["Janeiro   ", "Fevereiro", "Março     ", "Abril     ", "Maio     ", "Junho    ", "Julho    ", "Agosto   ", "Setembro   ", "Outubro   ", "Novembro", "Dezembro"]



def imprime_pluv(pluv):
        val = max(pluv)         # Obtem o maior valor da lista
        pos = pluv.index(val)   # obtem a posição do maior valor
        print(meses[pos],"\t", val)
        pluv[pos] = -1



def imprime_pluv_v2(pluv):
    pluv_ord = pluv.copy()  # cria copia da lista
    pluv_ord.sort()         # ordena a lista
    pluv_ord.reverse()
    for i in range(12):
        pos = pluv.index(pluv_ord[i])         # obtem posicao na lista original
        print(meses[pos],"\t", pluv_ord[i])   # para saber qual o mês que lhe corresponde
        pluv[pos] = -1


pluv = []
for i in range(12):   # ler pluviosidade ao longo dos 12 meses do ano
    valor = int(input("Pluviosidade no mês de {0} \t: " .format(meses[i])))
    pluv.append(valor)
imprime_pluv_v2(pluv)

input()