#3 Entrada de datos y manipulación. 
nombre = input("Ingrese su nombre completo: ") # Captura del nombre del usuario

# Recorre mediante un ciclo for el nombre al reves e imprimir cada letra
for letra in reversed(nombre):
    print(letra)
