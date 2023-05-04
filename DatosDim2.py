import random


class DatosDim2():

    def __init__(self, filas, columnas):
        self.datos = [[random.randint(2, 99) for j in range(filas)] for i in range(columnas)]

    def verMatriz(self):
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                print("[{}]".format(self.datos[i][j]), end="")
            print()

    def suma(self):
        acum = 0
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                acum += self.datos[i][j]
        return acum

    def resta(self):
        acum = 0
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                acum -= self.datos[i][j]
        return acum

    def sumaXFilas(self):
        resul = [0] * len(self.datos)
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                resul[i] += self.datos[i][j]
        return resul

    def sumaXCol(self):
        resul = [0] * len(self.datos[0])
        for j in range(len(self.datos[0])):
            for i in range(len(self.datos)):
                resul[j] += self.datos[i][j]
        return resul

    def verArreglo(self):
        capa = self.datos
        numFilas = len(capa)
        numCol= len(capa[0])
        arregloDosDim = []
        for columnas in range(numCol):
            arregloDosDim.append(capa[0][columnas])
        for filas in range(1, numFilas):
            arregloDosDim.append(capa[filas][numCol - 1])
        for columnas in range(numCol - 2, -1, -1):
            arregloDosDim.append(capa[numFilas - 1][columnas])
        for filas in range(numFilas - 2, 0, -1):
            arregloDosDim.append(capa[filas][0])

        return arregloDosDim
