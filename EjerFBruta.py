def selec_ordenar(valor):
    for i in range(len(valor)):
        for  j in range(i, len(valor)):
            if valor[i] > valor[j]:
                valor[i], valor[j] = valor[j], valor[i]

lista = [64, 25, 12, 22, 11]
print("Lista Original: ",lista )
selec_ordenar(lista)
print("Lista Ordenada: ",lista)
