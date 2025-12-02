#Llamar un mensaje cada que se requiera     #A

def saludar_usuario():
    print("¡Hola! Este es un mensaje de bienvenida.")
saludar_usuario()

#Funcion con parámetro sin retorno    #B    
def nombre_usuario(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al programa.")
nombre_usuario("Adrián")

#Crea una función con parámetros y retorno      #C
def calcular_iva(valor_venta):
    iva = valor_venta * 0.19
    return iva
print(f"El IVA calculado es: {calcular_iva(100000)}")


#Calcular el IVA a partir de un subtotal ingresado por el usuario con def   #D
def iva_usuario():
    subtotal = float(input("Ingrese el subtotal de la venta: "))
    iva = subtotal * 0.19
    return iva
print(f"El IVA para el subtotal ingresado es: {iva_usuario()}")


#Calcular las ventas con varios parametros y retorno    #E
def calcular_total(subtotal, iva):
    total = subtotal + iva
    return total
print(f"El total de la compra es: {calcular_total(100000, calcular_iva(100000))}")



#RETOS INICIALES

#Funcion que reciba tres numeros y devuelva la suma #0
def sumar_tres_numeros(num1, num2, num3):
    suma = num1+num2+num3
    return suma
print(f"La suma de los tres números es: {sumar_tres_numeros(5, 10, 15)}")



#Funcion que reciba tres numeros ingresados por el usuario y devuelva la suma #1
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
def sumar_tres_numeros_usuario(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3
    return suma
print(f"La suma de los tres números ingresados es: {sumar_tres_numeros_usuario(numero1, numero2, numero3)}")



#Funcion que reciba los pasajes diarios y devuelva la suma  #2
def pasajes_diarios(pasajeLun, pasajeMar, pasajeMie, pasajeJue, pasajeVie, pasajeSab):
    total_pasajes = pasajeLun + pasajeMar + pasajeMie + pasajeJue + pasajeVie + pasajeSab
    return total_pasajes
print(f"El total de los pasajes gastados es de: {pasajes_diarios(1000,2000,3000,4000,5000,6000)}")



#Funcion que reciba el precio unitario y la cantidad vendida y devuelva el total de la venta    #3
def precio_unitario(unitario,cantVendida):
    total_ventas= unitario * cantVendida
    return total_ventas
print(f"El total de la venta es de: {precio_unitario(1500,3)}")



#Funcion que reciba el costo unitario y el precio de venta y devuelva las ganancias  #4 
def costos_unitarios(CostUnitario, precioVentas):
    ganancias = precioVentas - CostUnitario
    return ganancias
print(f"Las ganancias totales fueron de: {costos_unitarios(2000,3000)}")



#total a pagar de una nómina, dado el valor por hora, la cantidad de horas trabajadas, las deducciones de fondo de empleados, otras deducciones, mientras el empleado esté activo:
def calcular_nomina(valor_hora, horas_trabajadas, deducciones_fondo, otras_deducciones, empleado_activo):
    if empleado_activo:
        salario_bruto = valor_hora * horas_trabajadas
        total_deducciones = deducciones_fondo + otras_deducciones
        salario_neto = salario_bruto - total_deducciones
        return salario_neto
    else:
        return "No se paga nómina a empleados inactivos"
print(f"El total a pagar de la nómina es: {calcular_nomina(20000, 160, 50000, 20000, False)}")



#Funcion que reciba el precio original y el descuento y devuelva el precio con descuento  #6
def precio_original(PrecioOriginal, Descuento):
    precio_con_descuento = PrecioOriginal - Descuento
    return precio_con_descuento
print(f"El precio total con descuento es: {precio_original(20000,5000)}")


#Funcion que reciba el precio original y el descuento en porcentaje y devuelva el precio con descuento  #6
def precio_con_descuento(PrecioOriginal, DescuentoPorcentaje):
    descuento = PrecioOriginal * (DescuentoPorcentaje / 100)
    return PrecioOriginal - descuento
print(f"El precio total con descuento es: {precio_con_descuento(20000,25)}")


#calcule el saldo final del inventario teniendo en cuenta esta recibe 4 parámetros y que saldo final inventario= Saldo inicialmes + cantidadesCompradas- cantidades vendidas y cantDadaDeBaja.
def saldo_final(SaldoInicial, CantidadesCompradas, CantidadesVendidas, CantidadesDadasBaja):
    return SaldoInicial + CantidadesCompradas - CantidadesVendidas - CantidadesDadasBaja
print(f"El saldo final del inventario es: {saldo_final(100, 50, 30, 10)}")