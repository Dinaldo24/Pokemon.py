def busq_fuer_bruta(lista,objet):
    for i in range(len(lista)):
        if lista[i] == objet:
            return i #si encuentra el objetivo retorna la posicion
    return -1 #retorna a -1 si no lo encuentra 
num = [10,23,45,70,11,15]
objet= 10

result = busq_fuer_bruta(num, objet)

if result != -1:
    print(f"El número encontrado en la posicion {result}")
else:
    print("El número buscado no se encuentra en la lista")


def duplicados(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i+1,n):
            if lista[i] == lista [j]:
                return "Verdadero" "Se encontro duplicado"
    return "Falso"

lista1 = [1,2,3,4,5,6] #No existe valores duplicados 
lista2 = [1,2,3,4,2,5] #Si existen Valores duplicados 

print(duplicados(lista1))
print(duplicados(lista2))
