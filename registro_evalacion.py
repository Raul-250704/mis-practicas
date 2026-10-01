def mostrar_encabezado_escuela():
    print(f"Univercidad Tecnologica de Xicotepec")
    print(f"Registro y Evalucion de Calificaciones")
mostrar_encabezado_escuela()

def obtener_nota_minima_aprobatoria():
    return 6.0
obtener_nota_minima_aprobatoria()

def evaluar_redmimiento(nota):

    if nota < 7.0:
        return"Reprobado"
    elif nota >=7 or nota<= 9.4:
        return"Aprovado"        
    elif nota >= 9.5 or nota == 10:
        return"Exelente"

resultado= evaluar_redmimiento(8)
print(resultado)

def calcular_promedio_ponderado(nota_examenes,nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas*0.30)
    return round(promedio, 1)
resultado = calcular_promedio_ponderado(9,10)
print("El promedio es :",resultado)
print()
def generar_boleta(nombre_alumno,nota_examenes,nota_tareas):
    nota_final= calcular_promedio_ponderado(nota_examenes,nota_tareas)
    nota_minima= obtener_nota_minima_aprobatoria()
    estado = evaluar_redmimiento(nota_final)

    print("--Boleta de Calificaciones--")
    print("Alumno : ", nombre_alumno)
    print("Nota Final :", nota_final)
    print("Estado :" , estado)

    if nota_final < nota_minima:
        return"Necesitas presentar el exemen extraordibario"
    else:
        return"En hora buena , exelente desempeño"    

boleta=  generar_boleta("Raul Gonzalez", 8,10)
print(boleta)