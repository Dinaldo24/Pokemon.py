def burbuja (arr):
    n = len (arr)
    for i in range(n): #Bucle externo de n interaciones
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j +1], arr[j]
    return arr

lista = [5,1,4,2,8]
print(f"Lista Original: {lista}")
print(f"Lista Ordenada: {burbuja(lista)}")
