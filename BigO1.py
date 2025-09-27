def busq_fuer_bruta(lista,objet):
    for i in range(len(lista)):
        if lista[i] == objet:
            return i #si encuentra el objetivo retorna la posicion
    return -1 #retorna a -1 si no lo encuentra 

ing = input("Ingrese lista de números ")
lis_ing = [int(num.strip ()) for num in ing.split(',')]

objet = int (input("Indique el numero a buscar: "))
result = busq_fuer_bruta(lis_ing, objet)

if result != -1:
    print(f"El número encontrado en la posicion {result}")
else:
    print("El número buscado no se encuentra en la lista")