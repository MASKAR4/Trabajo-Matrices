from DatosDim1 import *
from DatosDim2 import *
from DatosDim3 import *

datos = None


# ==[GUI]=======
def crear():
    x = int(input('Cuantas filas desea?: '))
    y = int(input('Cuantas columas desea?: '))
    z = int(input('Cuantas capas desea?: '))
    datos = DatosDim3(x, y, z, 0)
    # solucitar los valores
    for k in range(z):
        for i in range(x):1
            for j in range(y):
                nuevoValor = int(input(f'datos[{i}][{j}][{k}]='))
                datos.cambiarValor(i, j, k, nuevoValor)


return datos

             


# ==========
if __name__ == '__main__':
    datos = crear()
    datos.ver()
    print(f' La suma es: {datos.sumar()}')

    # datos = DatosDim1(3, "A")
    datos = DatosDim2(3, 3, "A")
    # datos = DatosDim3(3,3,3, "A")
    # datos.ver()
    # datos.darValor(1,2,1,"Z")
    # datos.ver()
