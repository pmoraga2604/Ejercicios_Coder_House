class Cliente():
    def __init__(self, nombre, apellido, sexo, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.dni = dni
        self.sesion_id = None
        self.monto_total = 0 

    def agrega_productos(self, Producto_Pinturas, cantidad):
        if Producto_Pinturas:
            stock_disponible = Producto_Pinturas.inventario - Producto_Pinturas.reserva_producto

            if stock_disponible >= cantidad:
                carrito = Producto_Pinturas.generar_compra(self.dni, cantidad)
                if carrito:
                    self.monto_total += carrito.precio * cantidad
                    print(f'Se agregaron {cantidad} unidades de {Producto_Pinturas.nombre} ({Producto_Pinturas.tipo}) al carrito de {self.nombre}')
                    print(f'Stock disponible de {Producto_Pinturas.nombre}: {stock_disponible - cantidad}')
                else:
                    print('No es posible agregar la cantidad solicitada')
            else:
                print(f'No hay suficiente stock de {Producto_Pinturas.nombre}. Stock disponible: {stock_disponible}. Cantidad solicitada: {cantidad}')
        else:
            print('No es posible agregar el producto')

    def valida_stock(self, Producto_Pinturas):
        if Producto_Pinturas:
            print(f'El stock disponible de {Producto_Pinturas.nombre} ({Producto_Pinturas.tipo}) es: {Producto_Pinturas.inventario - Producto_Pinturas.reserva_producto}')

class Producto():
    def __init__(self, id, marca, tipo, precio, inventario):
        self.id = id
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        self.inventario = inventario
        
# CLASES DERIVADOS DEL PRODUCTO (CON HERENCIA)
class Producto_Pinturas(Producto):
    def __init__(self, id, nombre, marca, precio, tipo, color, inventario):
        super().__init__(id, marca, tipo, precio, inventario)
        self.nombre = nombre  
        self.color = color
        self.reserva_producto = 0  

    def generar_compra(self, dni, cantidad):
        if self.reserva_producto + cantidad > self.inventario:
            return None
        else:
            agrega_carrito = Carrito(self.nombre, self.marca, self.precio, self.tipo, self.color, dni, cantidad)
            self.reserva_producto += cantidad
            return agrega_carrito
        
class Carrito(Producto_Pinturas):
    def __init__(self, nombre, marca, precio, tipo, color, dni, cantidad):
        super().__init__(1, nombre, marca, precio, tipo, color, 1)  
        self.dni = dni
        self.sesion_id = 1
        self.cantidad = cantidad

    def __str__(self):
        return str(self.cantidad)
