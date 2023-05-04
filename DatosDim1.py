import random


class DatosDim1():

    def __init__(self, filas):
        self.datos = [[random.randint(2, 1000) for j in range(filas)]]

    def verMatriz(self):
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                print("[{}]".format(self.datos[i][j]), end="")
            print()

    def resta(self):
        acum = 0
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                acum -= self.datos[i][j]
        return acum

    def suma(self):
        acum = 0
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                acum += self.datos[i][j]
        return acum

    def sumaXFilas(self):
        resul = [0] * len(self.datos)
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                resul[i] += self.datos[i][j]
        return resul
