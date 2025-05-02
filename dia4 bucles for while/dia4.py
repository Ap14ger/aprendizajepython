#  for Se usa con secuencias como range(), listas, cadenas, etc.


# for i in range(10):
#     if i == 5: #cuando i llegue a 5 pare o  termine el for 
#         continue #salta a lo siguiente que hay por ejecutar
#     print(i)
    
    
#while se ejecuta mientras la condicion sea verdadera ejemplo mientras contador sea menor o igual a 5 imprimira hasta llegar a 5 se usa cuando no se sabe cuantas veces ess nesesario repetir el buble 

# contador= 1
# while contador <= 5:
#     print(contador)
#     contador +=1
    
#toca colocar contador mas uno para que no se torne bucle infinito

#reto pedir numero a usuario y crea tabla de multiplicar

# numero = int(input("dame un numero para ver su tabla de multiplicar  "))


# for i in range(1,11):
#     resultado = numero* i
#     if resultado == 50:
#         break
#     print(f"{numero}* {i}={resultado}")
    
#el while se usa cuando no se sa
suma= 0    

#aqui el bucle esta infinito y sañe cuando la persona inserta el cero 
while   True:
    numero =int(input("Ingrese numeros"))
    if numero < 0:# esto significa si el numero es negativo dile numero no valido 
       print("numero no valido")
       continue
    elif numero == 0: #cuando inserte cero sal 
        break
    
    suma += numero
    print(f"la suma total de los posititvos es  {suma}")