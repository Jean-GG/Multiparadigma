#5 Manejo de informacion 

def imprimir_info(**datos):
    for llave, valor in datos.items(): #Recorre los elementos y los imprime
        print(f'"{llave}": "{valor}"')

# Ejemplo de uso
imprimir_info(nombre="Jean", edad=22, carrera="Ingeniería", semestre=10)
