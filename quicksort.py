lista= [1,3,66,4,2,6,7,10,5,2,3,-3,7]

def particion(lista):
    pivote = lista[0]
    menores =[]
    mayores =[]

    for i in range(1,len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    
    return menores , pivote , mayores


def quicksort(lista):
    if len(lista)<2:
        return lista
    
    menores,pivote,mayores=particion(lista)

    return quicksort(menores) + [pivote] + quicksort(mayores)


print(quicksort(lista))