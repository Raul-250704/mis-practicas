import datetime
def salular():
    print("Hola,Bienvenid@s")
salular()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime(%H:%M:%S)
    print(F"La hora actual es : {hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print(f"El area del triangulo es : {resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre} , tienes {edad} años")
saludar_persona("Raul", 20)

#Funciones con parametros
def calcular_premedio(cal1,cal2,cal3,cal4):
    res=(cal+cal2+cal3+cal4)/4
    return res
promedio=calcular_premedio(10,8,9,8)
print(f"El promedio del alumno es : {promedio}")

def calcular_precio(producto, cantidad , precio):
    monto=(precio*cantidad)
    return monto
recibo=calcular_precio("laptop" , 5, 12000)
print(f"El monto a pagar es : {recibo}")

#Funciones sin parametros

def despedida()
    print("Gracias por usar la aplicacion , Regrese pronto")
despedida()

def suma():
    print(10+5)
suma()