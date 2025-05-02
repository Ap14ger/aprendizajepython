nombre = input("Por favor ingrese su nombre ")
edad = int(input("Por favor ingrese su edad "))
estatura = float( input("Por favor ingrese su estatura "))
pregunta = input("Tiene experiencia previa programando? ")


#print(f"Hola mi nombre es {nombre}, mi edad es {edad} años y en 3 años tendre {edad + 3} , mi estatura es {estatura} y {pregunta} tengo experiencia programando")
print(f"Hola {nombre} tu edad es {edad} años y en 5 años tendras {edad + 5}")

altura=estatura
if altura > 1.80:
    print(f"su estatura de {altura} esta por encima del promedio mundial")
elif altura < 1.50:
    print(f"Su estatura de {altura} esta por debajo del promedio mundial")
else:
    print(f"Tu estatura {altura} esta dentro del promedio mundial")
    
respuesta = pregunta.lower()
if (respuesta == "si" ):
    print(f"te felicito sigue asi ")
else:
    print("Seria bueno que estudies")

