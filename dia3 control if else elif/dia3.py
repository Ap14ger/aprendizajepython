#  🔹 if, elif, else Sirven para que el programa tome decisiones según condiciones. reto pedir nombre edad imprimir y decidir 

nombre = input("dame tu nombre ").lower()
edad = int(input("dame tu edad "))


if edad < 12:
    print(f"hola {nombre} eres un niño ")
elif    13 <= edad <= 17:
    print(f"hola {nombre} eres un adolecente ")
elif edad >= 18:
    if nombre =="lucas" and edad==18:
        print(f"hola {nombre} justo estas entrando en  la adultez")
    else:
        print(f"hola {nombre} eres un adulto") 
else:
    print("operacion invalida")