

# nombre = input("Ingrese su nombre ")
# peso = float(input("Ingrese su peso "))
# estatura= float(input("Ingrese su estatura "))

# Imc =round(peso / (estatura ** 2),2)

# print(f"{nombre}, tu IMC es {Imc} ")

# if Imc < 18.5:
#     print(f"Hola {nombre} Su peso esta bajo")
# elif Imc < 25:
#     print("Esta dentro del peso normal")
# elif Imc < 30:
#     print("Tiene sobrepeso")
# else:
#     print("Todo esta bien")
    
    
def verificar_edad(nombre,edad):
    if edad >18:
        print("eres mayor de edad ")
    else:
        print("eres menor de edad ")
        
for i in range (3):     
    print(f"\nPersona {i+1}:")
    nombre = input("ingrese su nombre ")
    edad= int(input("Ingrese su edad "))


    verificar_edad(nombre,edad)