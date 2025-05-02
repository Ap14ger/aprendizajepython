#Un diccionario es una colección desordenada de elementos en pares clave:valor.

# persona={
#     #clave  valor
#     "nombre": "juan",
#     "edad": 30,
#     "email": "juanpepe@gmail.com",
#     "telefono": 325,
# }

#para aceder a elementos de diccionario
#print(persona["nombre"]) #juan

#tambien se puede usar .get() que no lanza error si no existe la clave
#print(persona.get("carro"," no registrado")) #si hay clave imprime el dato de la clave si no hay imprime no registrado

#metodos comues
# print(persona.keys())#obtener claves
# print(persona.values()) #obtener valor
# print(persona.items())#obtener clave valor

#un set es una coleccion desordenada de elementos unicos 
#con llaves
# mi_set={1,2,3,4}

# #con construtor
# otro_set=set([2,4,6])
# #metodos comunes 
# mi_set.add(5) #agrega elemento
# mi_set.discard(2)# elimina un elemento sin error si no existe

# Diccionario para guardar contactos
agenda = {}

# Set para guardar números ya usados
telefonos_usados = set()

while True:
    print("\n--- Menú ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Ver agenda")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")

        if telefono in telefonos_usados:
            print("❌ Ese número ya está asignado a otro contacto.")
        else:
            # Si el contacto ya existe, quitamos su número anterior del set
            if nombre in agenda:
                telefonos_usados.discard(agenda[nombre])
            
            # Guardamos el nuevo número
            agenda[nombre] = telefono
            telefonos_usados.add(telefono)
            print("✅ Contacto guardado.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        if nombre in agenda:
            print(f"📞 {nombre}: {agenda[nombre]}")
        else:
            print("⚠️ Contacto no encontrado.")

    elif opcion == "3":
        print("\n📒 Agenda:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
        if not agenda:
            print("La agenda está vacía.")

    elif opcion == "4":
        print("👋 ¡Hasta luego!")
        break

    else:
        print("❌ Opción no válida.")
