#4 Entrada de datos y estructuración. 
materias = {}

# Solicitar las materias que desea capturar
cantidad = int(input("Cuantas materias quieres registrar? "))
for i in range(cantidad): # Uso del ciclo for para capturar el numero de materias registrado
    nombre = input(f"Ingrese el nombre de la materia: ")
    creditos = int(input(f"Ingrese los creditos de {nombre}: "))
    materias[nombre] = creditos

# Imprimir
print("\nMaterias registradas:")
for materia, creditos in materias.items():
    print(f"{materia} tiene {creditos} creditos.")

total_creditos = sum(materias.values()) #Suma de los creditos
print(f"\nEl numero total de creditos de este semestre son: {total_creditos}")
