import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]] )
#Suma de matricez
suma = A+B
print("--SUMA A+B")
print(suma)

#Multiplicacion de elementos
prod_elem=A+B
print("---MuLTIPLICACION A+B---")
print(prod_elem)
#Producto matricial
prod_mat = A@B
print("--PRODUCTOS MATRICIOANL---")
print(prod_mat)
#Transpuesta
transpuesta = A.T
print("----transpuesta a----")
print(transpuesta)
#DETERMINANDITE Y INVERSA
det = np.linalg.det(A)
inv = np.linalg.inv(B)
print("DETERMINANTE A")
print(det)
print("INVERSA A")
print(inv)