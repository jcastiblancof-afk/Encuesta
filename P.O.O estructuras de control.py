#diseñar una encuesta para 6 personas (nombre, carrera, idea de proyecto)
def encuesta():
    for i in range (6):
        nombre = str(input("¿Cual es tu nombre?"))
        carrera = str(input("¿Cual es tu carrera?"))
        idea_de_proyecto = str(input("¿Cual es tu idea de proyecto?"))

for x in range (6):
    print (f"encuestado {x}")
    print (f"Nombre: {nombre[x]}")