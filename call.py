from clases.constructores import Cliente, Producto_Pinturas

producto1 = Producto_Pinturas(1, 'True Color', 'Cerecita', 7.99, 'Pintura', 'Azul', 6)
producto2 = Producto_Pinturas(2, 'Cerestain', 'Soquina', 11.99, 'Latex', 'Verde', 9)
producto3 = Producto_Pinturas(3, 'Rapid Color', 'Cerecita', 3.99, 'Barniz', 'Incoloro', 3)

cliente1 = Cliente('Pedro', 'Moraga', 'Masculino', '38', '12342443-2')
cliente2 = Cliente('Julieta', 'Moraga', 'Femenino', '10', '18768763-2')
cliente3 = Cliente('Perico', 'Los Palotes', 'Masculino', '40', '1889763-2')

cliente1.agrega_productos(producto1, 3) 
cliente1.agrega_productos(producto2, 4) 
cliente1.agrega_productos(producto3, 1) 

cliente1.valida_stock(producto1) 
cliente1.valida_stock(producto2) 
cliente1.valida_stock(producto3)   

print(f"El monto total de la compra para {cliente1.nombre} es: {cliente1.monto_total}")

cliente2.agrega_productos(producto1, 1)  
cliente2.agrega_productos(producto2, 3)  
cliente2.agrega_productos(producto3, 1)  

cliente2.valida_stock(producto1)  
cliente2.valida_stock(producto2)  
cliente2.valida_stock(producto3)  

print(f"El monto total de la compra para {cliente2.nombre} es: {cliente2.monto_total}")

cliente3.agrega_productos(producto1, 3)
cliente3.agrega_productos(producto2, 2)
cliente3.agrega_productos(producto3, 1)

cliente3.valida_stock(producto1)  
cliente3.valida_stock(producto2)  
cliente3.valida_stock(producto3)  

print(f"El monto total de la compra para {cliente3.nombre} es: {cliente3.monto_total}")
