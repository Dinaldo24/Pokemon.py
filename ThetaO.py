def suma_pares(lista):
    sumtotal =0
    n = len(lista)
    for i in range(n):
        for  j in range(n):
            sumtotal += lista[i] + lista[j]
    return sumtotal

num = [1,2,3]
result = suma_pares(num)
print("Suma total de pares: ",result)