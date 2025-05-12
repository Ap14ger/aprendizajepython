# class Perro:
#     def __init__(self, nombre, edad):
#             self.nombre= nombre
#             self.edad =edad
            
        
    
#     def ladrar(self):
#         print(f"{self.nombre} dice guau")
        
        
# mi_perro= Perro("Toby" , 3) #instancia de la clase perro


# print(mi_perro.nombre)
# mi_perro.ladrar()



class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        
    def mostrar(self):
        print(f"{self.nombre} tiene una nota de {self.nota}")
        
#lista para guardar estudiantes
lista_estudiantes =[]



#pide al usuario el numero de estudiantes que quiere ingresar
cantidad=int(input("Cuantos estudiantes quiere ingresar: "))
#usa ciclo for para la cantida que quiere ingresar 
for i in range(cantidad):
    print(f"\nEstudiante {i+1}: ") #incrementa uno mas hasta completar el numero de estudiantes que quiere ingresar
    nombre=input("Nombre: ") #pide el nombre
    nota=float(input("Nota: ")) # pide la nota
    
    
    estudiante = Estudiante(nombre, nota)
    lista_estudiantes.append(estudiante) #Guarda en el diccionario de lista_estudiantes
    
#realiza la suma de la lista de estudiantes   
suma=0
print("\n-- Lista de estudiantes--")
for estudiante in lista_estudiantes:
    estudiante.mostrar()
    suma += estudiante.nota
    
#suma las notas y divide por el numero de la lista_estudiantes
promedio = suma / len(lista_estudiantes)
print(f"\nPromedio general: {promedio:.2f}")



#crea estudiantes estos son objetos
# e1 = Estudiante("Ana",4.5)
# e2 =Estudiante("luis",3.8)
# e3 =Estudiante("Luis", 5.0)

# #agrega a la lista
# lista_estudiantes.append(e1)
# lista_estudiantes.append(e2)
# lista_estudiantes.append(e3)
        
# #mostrar todos los estudiantes
# suma =0
# for estudiante in lista_estudiantes:
#     estudiante.mostrar()
#     suma += estudiante.nota
    
# #calcula promedio de los estudiantes 

# promedio= suma / len(lista_estudiantes)
# print(f"\nPromedio general: {promedio:.2f}")


# e2.mostrar()
# e1.mostrar()