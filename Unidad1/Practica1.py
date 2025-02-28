#1 Funciones con n parámetros
def calcularProd(*numeros):
 producto = 1
 for num in numeros:
  producto *= num
 return producto

resultado = calcularProd(2, 3, 4)
print(resultado)  # Salida: 24