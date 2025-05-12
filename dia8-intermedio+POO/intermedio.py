# comprension de listas Es una forma compacta y eficiente de crear listas en una sola línea de código, eliminando la necesidad de bucles for explícitos.
# cuadrados = [x**2 for x in range(5)] # 0,1,4,9,16
# print(cuadrados)


#La función enumerate() te da tanto el índice como el valor de los elementos de un iterable.
# nombres = ["Ana", "Luis", "Carlos"]
# for i, nombre in enumerate(nombres):
#     print(i, nombre)

# Funciones lambda ¿Qué es? Son funciones pequeñas y anónimas, definidas con la palabra clave lambda.
# doble = lambda x: x * 2
# print(doble(4))  # 8


#map filter reduce
#map aplica una funcion a todos los elementos de un iterable y dvuelve el iterable con los resultados

# numeros = [1,2,3,4]
# dobles = list(map(lambda x: x*2,numeros))

#filter filtra los elementos de un iterable, devolviendo solo aquellos que cumplen con una condicion

# numeros = [1,2,3,4]
# pares =list(filter(lambda x: x % 2 ==0, numeros))

# try/except permite capturar y manejar errores en el codigo de manera controlada,evita que el programa se cierre inesperadamente

# try:
#     resultado = 10 /0  #eeor 
# except ZeroDivisionError:
#     print("No se puede dividir entre 0")
# else:
#     print("Todo salio bien")
# finally:
#     print("Este bloque siempre se ejecuta")


#decorador mdifica el comportamientos de otra funcion sirve para reutilizar codigo

# def decorador(func):
#     def wrapper():
#         print("Antes de ejecutar la funcion")
#         func()
#         print("Despues de ejecutar la funcion ")
#     return wrapper

# @decorador
# def saludar():
#     print("Hola!") #hace que ppueda imprimir hola dentro de wrapper
    
# saludar()

# from poo import suma

# print(suma(2,5)) #trae del modulo poo

#reto
# nombre=input("inserte su nombre")
# hora=float(input("Inserte numeor de horas trabajadas"))
# precio=int(input("Cuanto es el precio por hora"))

# print(f"hola {nombre}")


# resultado=hora * precio
# print(f"{nombre} tu pago por las {hora} horas trabajadas es {resultado}")
    