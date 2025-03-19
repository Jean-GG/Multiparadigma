#Libreria para hacer pruebas unitarias
import unittest

class Producto:
    def __init__(self, nombre, precio, stock): # Constructor
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    # Metodo que devuelve el coste del producto
    def calcular_costo(self):
        return self.precio
    
    # Devuelve informacion del producto
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class ProductoFisico(Producto): # Hereda de la clase padre Producto
    def __init__(self, nombre, precio, stock, costo_envio): # Constructor
        super().__init__(nombre, precio, stock) # Llamada al constructor Padre
        self.costo_envio = costo_envio

    # Metodo que calcula el costo del producto fisico
    def calcular_costo(self):
        return self.precio + self.costo_envio

class ProductoDigital(Producto):
    def __init__(self, nombre, precio, stock):
        super().__init__(nombre, precio, stock) # Llamada al constructor Padre

    # Metodo que calcula el costo del producto digital
    def calcular_costo(self):
        return self.precio - (self.precio * 0.1)

class Carrito:
    def __init__(self):
        self.productos = []
    
    # Metodo para agregar productos al carrito
    def agregar_producto(self, producto):
        if producto.stock > -1: #Valida si el producto es fisico o digital
            if producto.stock > 0: #Producto Fisico
                self.productos.append(producto)
                producto.stock -= 1
                print(f"{producto.nombre} agregado.")
            else:
                print("No hay stock.")
        else: #Producto Digital
                self.productos.append(producto)
                print(f"{producto.nombre} agregado.")
    
    # Metodo para calcular el total de todos los productos agregados al carrito
    def calcular_total(self):
        return sum(p.calcular_costo() for p in self.productos)
    
    # Devuelve la informacion de los productos agregados al carrito, 
    # si no hay productos devuelve "Carrito vacio"
    def __str__(self):
        return "\n".join(str(p) for p in self.productos) or "Carrito vacío"

class Tienda:
    def __init__(self):
        self.catalogo = []
    
    # Metodo para agregar producrtos al catalogo de la tienda
    def agregar_al_catalogo(self, producto):
        self.catalogo.append(producto)
        print(f"{producto.nombre} añadido al catálogo.")
    
    # Metodo que busca por nombre un producto en el catalgo de la tienda
    def buscar_producto(self, nombre):
        for producto in self.catalogo:
            if producto.nombre == nombre:
                return producto
        return None
    
    # Metodo para realizar la compra de todos los productos agregados al carrito
    def realizar_compra(self, cliente, carrito):
        if not carrito.productos:
            return "Compra cancelada: carrito vacío."
        total = carrito.calcular_total()
        return f"Compra de {cliente.nombre}:\n{carrito}\nTotal: ${total}"

class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    # Devuelve informacion sobre el cliente
    def __str__(self):
        return f"{self.nombre} - ${self.correo}"

# Prueba unitaria
class TestCarrito(unittest.TestCase):
    def test_calcular_total(self):
        tienda = Tienda()

        # Crear productos
        producto1 = ProductoFisico("Celular", 1000, 5, 50)
        producto2 = ProductoDigital("Manga Digital", 20, -1)
        producto3 = ProductoFisico("Memoria Ram", 600, 7, 30)

        # Agregar productos al catalogo
        tienda.agregar_al_catalogo(producto1)
        tienda.agregar_al_catalogo(producto2)
        tienda.agregar_al_catalogo(producto3)
        
        # Crear carrito y agregar productos
        cliente = Cliente("Jean", "jean@gmail.com")
        carrito = Carrito()
        carrito.agregar_producto(tienda.buscar_producto(producto1.nombre))
        carrito.agregar_producto(tienda.buscar_producto(producto2.nombre))
        carrito.agregar_producto(tienda.buscar_producto(producto3.nombre))

        #Imprimir el ticket
        print("----------------------------------------------------------------------")
        print(tienda.realizar_compra(cliente, carrito))
        
        # Calcular total esperado
        total_esperado = producto1.calcular_costo() + producto2.calcular_costo() + producto3.calcular_costo()
        
        # Verificar que el total calculado sea correcto
        self.assertEqual(carrito.calcular_total(), total_esperado)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)