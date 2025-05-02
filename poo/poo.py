class Persona:
    
    def inicializar(self,nom):
        self.nombre=nom
        
    def imprimir(self):
        print("Nombre",self.nombre)
        
        
#bloque principal
Persona1=Persona()
Persona1.inicializar("pedro")
Persona1.imprimir()


Persona2=Persona()
Persona2.inicializar("juan")
Persona2.imprimir() 

persona3=Persona()
persona3.inicializar("pepe")
persona3.imprimir()