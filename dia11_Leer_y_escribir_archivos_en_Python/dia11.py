# ¿Qué son los archivos .txt y .csv?📄 .txt:Son archivos de texto plano, como los que abres con el Bloc de Notas. Puedes guardar ahí cualquier texto: frases, listas, mensajes, etc.

#leer archivo 
import csv

# with open("notas.csv",newline='', encoding=utf-8) as archivo:
#     lector = csv.reader(archivo)
#     for fila in lector:
#         print(fila)


#lector notas

def leer_notas(dia11_leer_y_escribir_archivos_en_python):
    notas =[]
    with open(dia11_leer_y_escribir_archivos_en_python,newline='', encoding="utf-8") as archivo:
        lector =csv.reader(archivo)
        next(lector)
        for fila in lector:
            nombre = fila[0]
            nota =float(fila[1])
            notas.append((nombre,nota))
    return notas


def mostrar_resultados(notas):
    total=0
    for nombre, nota in notas:
        print(f"{nombre} tiene una nota{nota}")
        total += nota
    promedio= total / len(notas)
    print(f"\nPromedio general: {promedio:.2f}")
    
    
notas=leer_notas("notas.csv")
mostrar_resultados(notas)