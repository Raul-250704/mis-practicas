#Creacion de una matriz de 3x3
matriz=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#acceso a los elementos: matriz [filas ][columnas]
print(matriz[1][2])#fila indice 1 columna  indice 2
#Modicar elementos
matriz[0][0]=100
for fila in matriz:
    for elementos in fila:
        print(elementos, end=" ")
    print()