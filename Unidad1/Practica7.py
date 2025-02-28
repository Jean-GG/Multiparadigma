#7 Formateo y conversiones 
from datetime import datetime

# Imprime el menu
print("1.- Imprimir YYYY/MM/DD")
print("2.- Imprimir MM/DD/YYYY")
eleccion = input("Seleccione una opcion: ")
hoy = datetime.today() #lo usamos para obtener la fecha actual

# Imprimir la fecha de acuerdo a la opcion seleccionada
formatos = {"1": hoy.strftime("%Y/%m/%d"), "2": hoy.strftime("%m/%d/%Y")} # Aqui estan los distintos formatos para la fecha
print(formatos.get(eleccion, "Opcion invalida"))
