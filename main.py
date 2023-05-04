from DatosDim1 import *
from DatosDim2 import *
from DatosDim3 import *

datos = None

def get_input():
    filas = int(input("Ingrese las filas deseadas: "))
    columnas = int(input("Ingrese las columnas deseadas: "))
    capas = int(input("Ingrese las capas deseadas: "))
    return filas, columnas, capas

if __name__ == '__main__':
    filas, columnas, capas = get_input()

#----------------------------------------
# Matriz una dimension
print("Matriz de una dimension")
print()
matriz1 = DatosDim1(filas)
matriz1.verMatriz()

print()

suma = matriz1.suma()
print("La suma de los elementos de la matriz es =", suma)

print()

resta = matriz1.resta()
print("La resta de los elementos de la matriz es =", resta)

print()

sumaFilas = matriz1.sumaXFilas()
print("Suma por filas")
for i in range(len(sumaFilas)):
 print("[{}]".format(sumaFilas[i]), end="")
 print()

# ----------------------------------------
# Matriz de dos dimensiones
print("\nMatriz de dos dimensiones\n")
matriz2 = DatosDim2(filas, columnas)
matriz2.verMatriz()

print("\nSuma de la matriz =", matriz2.suma())

print("\nResta de la matriz =", matriz2.resta())

print("\nSuma por filas:")
for i, suma in enumerate(matriz2.sumaXFilas()):
 print("Fila {}: {}".format(i+1, suma))

print("\nSuma por columnas:")
for i, suma in enumerate(matriz2.sumaXCol()):
 print("Columna {}: {}".format(i+1, suma))

sumaXFilas = sum(matriz2.sumaXFilas())
sumaXCols = sum(matriz2.sumaXCol())

print("\nTotal de la suma de filas: ", sumaXFilas)
print("Total de la suma de columnas: ", sumaXCols)

print("\nNúmeros en los bordes: ", matriz2.verArreglo())
# -------------------------------------------------------
# Matriz de tres dimensiones
print("Matriz de tres dimensiones")
matriz3 = DatosDim3(filas, columnas, capas)
matriz3.verMatriz()

# Suma y resta
print("\nSuma y resta:")
suma = matriz3.suma()
resta = matriz3.resta()
print("La suma es: ", suma)
print("La resta es: ", resta)

# Sumas por capas, filas y columnas
print("\nSumas por capas, filas y columnas:")
sumXCapas = matriz3.sumaXCapas()
sumXFilas = matriz3.sumaXFilas()
sumColumnas = matriz3.sumaXColumnas()
print("La suma de capas es: ", sumXCapas)
print("La suma de filas es: ", sumXFilas)
print("La suma de columnas es: ", sumColumnas)

# Bordes de la matriz
print("\nBordes de la matriz:")
bordesMatriz = matriz3.verBorde()
print("Los bordes son: ", bordesMatriz)
