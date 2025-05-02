# Una lista en Python es una colección mutable (puede cambiarse) de elementos.

# len(frutas)         # número de elementos
# frutas.append("uva") # añade
# frutas.pop()        # elimina el último
# frutas.sort()       # ordena

# frutas = ["manzana", "pera", "banano"]

# frutas.append("mango")



# tupla = (1, 2, 3, 4) # los tuplas no se pueden modificar 
# #tupla[0] = 10  --> Error: no puedes modificarla
# print(tupla[-1]) # d (índice negativo: empieza desde el final en este caso seria desde el 4)
# print(tupla)


# #  Slicing (rebanado)
# # Permite obtener una subsección de una lista o tupla.
# lista = ['a', 'b', 'c', 'd', 'e']

# print(lista[1:4])  # ['b', 'c', 'd'] -> desde el índice 1 al 3
# print(lista[:3])   # ['a', 'b', 'c'] -> desde el inicio hasta el índice 2
# print(lista[2:])   # ['c', 'd', 'e'] -> desde el índice 2 hasta el final
# print(lista[::2])  # ['a', 'c', 'e'] -> salto de 2 en 2


# # .append(x) → Agrega un elemento al final.

# .insert(i, x) → Inserta un elemento en la posición i.

# .remove(x) → Elimina el primer elemento igual a x.

# .pop(i) → Elimina y devuelve el elemento en la posición i.

# .index(x) → Devuelve el índice del primer elemento igual a x.

# .sort() → Ordena la lista (por defecto, de menor a mayor).

# .reverse() → Invierte el orden de la lista.



# For anidados
# Cuando tienes listas dentro de listas (listas anidadas) o quieres hacer combinaciones, puedes usar bucles for dentro de for.

# Ejemplo básico:

# # # python
# # # Copiar
# # # # Editar
# pantalones= ['jeans','pntalon formal','short']
# camisas=['camisa blanca','camiza azul','camiseta negra']
# for pantalon  in pantalones:        # Primer for
#    for camisa in camisas:    # Segundo for (anidado)
#     print(f"Combina {pantalon} con {camisa}")
        
        
#ejemplo con listas anidadas
# ordena la lista de la matriz
# matriz=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end='')
        
        
# Concepto | ¿Mutable? | ¿Cómo se crea? | Ejemplo
# Lista | Sí | [] | [1, 2, 3]
# Tupla | No | () | (1, 2, 3)



# estudiantes= [
#     ('Ana', [4.5,3.8,5.0]),
#     ('Luis', [4.2,3.2,3.5]),
    
# ]
 
# for estudiante in estudiantes:
#     nommbre= estudiante[0]
#     notas=estudiante[1]
    
    
#     print(f"\nNotas de {nommbre} :")
    
#     for nota in notas:
#         print(f" - {nota}")
        
#         promedio = sum(notas)/ len (notas)
#         print(f"Promedio : {promedio:.2f}")
        
# 🔥 Cosas que usamos aquí:

# Concepto	¿Dónde lo usamos?
# Listas	estudiantes es una lista principal
# Tuplas	Cada estudiante es una tupla (nombre, notas)
# Indexación	estudiante[0] para nombre, estudiante[1] para notas
# Slicing	Podríamos hacer slicing para, por ejemplo, solo ver las 2 primeras notas
# Métodos de lista	Usamos sum() y len() para operar sobre la lista de notas
# For anidados	Un for para cada estudiante y un for dentro para recorrer sus notas


pantalones=['pantalon jean','pantalon clasico','pantalon dril']
camisas=['camsia mangalarga','camisa manga corta','camisa clasica','buso']
calificaciones= [4.0,2.5,3.9,5.0]
oufits=[]

for pantalon in pantalones:
    for i, camisa in enumerate(camisas):
        oufit=f"{pantalon}+{camisa}"
        calificacion=calificaciones[i]
        oufits.append((oufit,calificacion))
        
oufits.sort(key=lambda x: x[1], reverse=True)

       
       
respuesta= input("Quieres ver solo los outfis con 4 estrellas(si/no): ")

if respuesta.lower()=="si":
    for outfit, calificacion in oufits:
        if calificacion > 4.0:
            print(f"{outfit} {calificacion} estrellas")
else:
    for oufit, calificacion in oufits:
        print(f"estas son las calificaciones {calificaciones}")