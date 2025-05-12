#Manejo de errores en Python: try, except, finally

# try se usa para evitar que el programa se bloquee al haber un error
# except que hacer si ocurre un erro 
# finally codigo que se ejecuta siempre haya error o no


#ejemplo

# try:
#     numero=int(input("Ingresa un numero"))
#     resultado= 10/numero
#     print("resultado: ", resultado)
# except ZeroDivisionError:
#     print("Debes ingresar un numero valido.")
# except ZeroDivisionError:
#     print("No puedes dividir entre cero")
# finally:
#     print("Fin del programa")

# valida isalpha que solo sean letras  y la edad no puede ser menor a 0
# def validar_datos():
#     try:
#         nombre = input("Ingresa tu nombre: ")
#         if not nombre.isalpha():
#             raise ValueError("El nombre de contener solo letras.")
        
        
#         edad=int(input("Ingresa tu edad: "))
#         if edad<0:
#             raise ValueError("La edad no puede ser negativa.")
        
#         print(f"Nombre {nombre}, Edad: {edad}")
        
        
#     except ValueError as error:
#         print ("Erorr:",error)
        
#     finally:
#         print("Validacion terminada")
        
# validar_datos()


from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<form method="post">
  Nombre: <input name="nombre"><br>
  Edad: <input name="edad"><br>
  <button>Validar</button>
</form>
<p>{{ mensaje }}</p>
'''

@app.route("/", methods=["GET", "POST"])
def validar():
    mensaje = ""
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            edad = int(request.form["edad"])
            if not nombre.isalpha():
                raise ValueError("Nombre inválido.")
            if edad < 0:
                raise ValueError("Edad inválida.")
            mensaje = f"✅ Bienvenido, {nombre} ({edad})"
        except ValueError as e:
            mensaje = f"❌ Error: {e}"
    return render_template_string(HTML, mensaje=mensaje)

app.run(debug=True)
