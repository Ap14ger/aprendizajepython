#Es un paradigma que te permite organizar tu código en "clases" que representan entidades con datos y comportamientos (métodos o funciones). Ideal para proyectos grandes y mantenibles.

# class Perro:
    #atributo de clase
    # especie='mamifero'
    # def __init__(self,nombre,raza):# El método __init__ es llamado al crear el objeto
    #     print(f"Creando perro {nombre}, de la raza {raza}")
        
        #atributos de instancia
        # self.nombre = nombre
        # self.raza= raza
        
        
    #metodos que es lo mismo que funciones
    # def ladra(self):
    #     print("Guau")
        
    # def camina(self,pasos):
    #     print(f"Caminando {pasos} pasos")



#objetos esto aplica para crear diferentes perros pero que perteneceran a la misma clase por ejemplo son mamiferos tiene cuatro patas tienen un nombre pertenecen a una raza se usa para no repetir variables
# mi_perro=Perro("toby","buldog")  #objeto de la clase perro osea una subclase 
# mi_perro.especie #todos los perros heredaran este atributo de la clase
# mi_perro.ladra()#llamadas a los metodos que queremos que tenga ese perro
# mi_perro.camina(10)
# otro_perro=Perro("cazador","aleman")
# otro_perro.camina(20)#uno camina 10 pasos y otr 20 y estamos reutilizando los metodos y la clase y tambien los atributos de la clase y los de la instancia



#encapsulamiento oculta detalles internos usando self.__atributo

# class CuentaBancaria:
#     def __init__(self,saldo):
#         self.__saldo=saldo # significa que es un atributo privado
        
#     def ver_saldo(self):
#         return self.__saldo
    
#     def depositar(self, cantidad):
#         if cantidad > 0:
#             self.__saldo+= cantidad
            
# cuenta=CuentaBancaria(100)
# cuenta.depositar(50)
# print(cuenta.ver_saldo())


#ahora veremos los tipos de metodos

# class Persona:
#     def __init__(self, nombre, edad):
#          self.nombre=nombre
#          self.edad=edad
        
#     def saludar(self):
#         print(f"Hola soy {self.nombre}, y tengo {self.edad} años")
        
# perosna1=Persona("ana",30)
# perosna1.saludar()


# HERENCIA  Una clase puede heredar de otra, reutilizando código esta hereda de persona.

# class Empleado(Persona):
#     def __init__(self, nombre, edad, cargo):
#         super().__init__(nombre, edad) #llama al contrutor de la clase padre en este caso seria la clase persona
#         self.cargo = cargo #nuevo atributo solo de la clase empleado
        
#     def mostrar_info(self):
#         print(f"{self.nombre}, soy {self.cargo}")
        
        
# e=Empleado("Luis", 25, "Desarrollador")
# e.saludar() #Hereda el metodo saludar
# e.mostrar_info()



# polimorfismo dos clases diferentes pueden usar el mismo metodo con comportamientos distintos

class Gato():
    def hablar(self):
        print("Miuau")
    
    
class Perro:
    def hablar(self):
        print("guau")
    
def hacer_hablar(animal):
    animal.hablar() #juntas usan el metodo hablar
    
hacer_hablar(Gato())
hacer_hablar(Perro())
    
    

def suma (a,b):
    return a +b
