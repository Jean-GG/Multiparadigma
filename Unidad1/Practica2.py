#2 Manejo y manipulación de elementos de una lista 
abecedario = [ #Arreglo que contiene el abecedario
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Se crea una nueva lista
listaABC = []

# Ciclo que nos ayuda a recorrer la lista
for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:
        listaABC.append(abecedario[i])

print(listaABC)