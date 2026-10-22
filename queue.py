from collections import deque
import time
cola = deque()
#Agregar elementos
cola.append("Caliente 1")
cola.append("Caliente 2")
cola.append("Caliente 3")
#Sacar el primer elemento atendido (desencolar)
atendido=cola.popleft()
#Mostar resultado
print("Atendido", atendido)
print("cola restante",cola)


cola_reproduccion=deque()
#Agregar elementos de reproduccion
cola_reproduccion.append("1.-Mochila azul")
cola_reproduccion.append("2.-Aerolinea Carriillo")
cola_reproduccion.append("3.-Beso")
cola_reproduccion.append("4.-Mujeres divinas")
cola_reproduccion.append("5.-La calabaza")
#Mostrar las canciones en espera
print("Canciones en espera.")
for cancion in cola_reproduccion:
    print("_", cancion)
    print("Iniciado reproduccion")

#Desencolar
while cola_reproduccion:
    cancion_actual= cola_reproduccion.popleft()
    print(f"Sonando ahora:{cancion_actual}")
    time.sleep(1) #Simula la duracion del tema
    print(f"Finzalizo:{cancion_actual}")

#Muestra cuantos canciones quedan en la cola
print(f"(Quedan :{len(cola_reproduccion)} canciones de la cola)")
print("La cola de reproduccion ha finalizado")

