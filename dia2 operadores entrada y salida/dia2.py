# #Operadores aritmeticos	Descripción	Ejemplo
# +	Suma	3 + 2 → 5
# -	Resta	5 - 1 → 4
# *	Multiplicación	4 * 3 → 12
# /	División	8 / 2 → 4.0
# //	División entera	9 // 2 → 4
# %	Módulo (resto)	7 % 3 → 1
# **	Potencia	2 ** 3 → 8

# Operadores logicos	Descripción	Ejemplo
# and	Verdadero si ambos lo son	True and False → False
# or	Verdadero si al menos uno lo es	True or False → True
# not	Invierte el valor	not True → False

# Operadores de comparacion	Significado
# ==	Igual a
# !=	Distinto de
# >	Mayor que
# <	Menor que
# >=	Mayor o igual que
# <=	Menor o igual que


#1 reto calculadora
# n1= float(input("Ingrese un numero "))
# n2= float(input("Ingrese un numero "))


# print("opciones suma,resta,multiplicacion,division")
# operacion= input("Elige la operacion a realizar ").lower()

# if operacion == "suma":
#     resultado = n1+n2
# elif operacion =="resta":
#     resultado = n1-n2
# elif operacion == "multiplicacion":
#     resultado = n1*n2
# elif operacion =="division":
#     if n2 !=0:
#         resultado = n1/n2
#     else:
#         print("operacion invalida")
# else:
#     print("Toma una opcion")
    
    
# print(f"El resultado de la {operacion} es {resultado}")

#2 reto validacion con operador logico and y not y or

# nombre= input("Escribe tu nombre ")
# edad = int(input("Cual es tu edad "))

# print("Roles disponibles, admin, usuario, invitado,gerente")
# rol= input("Elige el rol ").lower()

# if edad > 18 and rol == "admin":
#     print("Bienvenido administrador")
# elif nombre == "juan"and rol=="gerente" and edad == 25:
#     print(f"Bienvenido Gerente {nombre} a su empresa")
# elif not rol =="invitado" and edad > 18:
#     print(f"Bienvendido {nombre}, su rol es {rol}")
# else:
#     print("Error") 
    
    
# nombre = input("Ingrese su nombre: ")
# edad = int(input("ingrese su edad: "))
# contraseña= ( input("Ingrese su contraseña: "))

# print("Roles disponibles admin,usuario,invitado,supervisor")
# rol=input("Elige tu rol ").lower()

# if (nombre=="ana"or nombre=="pedro" )and rol == "supervisor":
#     if contraseña == "clave123":
#         print(f"Bienvenido(a) {nombre} ")
#     else:
#         print("error no eres el supervisor")
# elif edad >= 18 and  not rol== "invitado":
#     if contraseña == "clave123":
#         print(f"Bienvenido {nombre} acceso permitido su rol es {rol} ")
#     else:
#         print("contraeña incorrecta")
# else:
#         print(f"Hola {nombre} tu contraseña  o edad no estan dentro de lo permitido")

# n1 = int(input("dame un numero "))
# n2 = int(input("dame un numero "))

# print("operaciones disponibles(suma,resta,multiplicacion,division)")

# operacion=input("que operacion vas hacer ")

# if operacion == "suma":
#     print(f"el resultado es {n1+n2}")
# elif operacion =="resta":
#     print(f"el resultado es {n1-n2}")
# elif operacion == "multiplicacion":
#     print(f"el resultado es {n1*n2}")
# elif operacion =="division":
#     if n2 !=0:
#         print(f"el resultado es {n1/n2}")
# else:
#     print("operacion invalida")