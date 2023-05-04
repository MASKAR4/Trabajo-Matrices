import random


class DatosDim3():

    def __init__(self, filas, col, capas):
        self.datos = [[[random.randint(0, 1000) for k in range(col)] for j in range(filas)] for i in range(capas)]


    def verMatriz(self):
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                print("")
                for k in range(len(self.datos[i][j])):
                    print("[{}]".format(self.datos[i][j][k]), end="")
            print()

    def suma(self):
        acum = 0
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                for k in range(len(self.datos[i][j])):
                    acum += self.datos[i][j][k]
        return acum

    def resta(self):
        acum = 0
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                for k in range(len(self.datos[i][j])):
                    acum -= self.datos[i][j][k]
        return acum

    def sumaXCapas(self):
        resul = [0] * len(self.datos)
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                for k in range(len(self.datos[i][j])):
                    resul[i] += self.datos[i][j][k]
        return resul

    def sumaXFilas(self):
        resultado = []
        for capas in range(len(self.datos)):
            capaActual = []
            for filas in range(len(self.datos[capas])):
                sumaFila = 0
                for columnas in range(len(self.datos[capas][filas])):
                    sumaFila += self.datos[capas][filas][columnas]
                capaActual.append(sumaFila)
            resultado.append(capaActual)
        return resultado

    def sumaXColumnas(self):
        resultado = []
        for capas in range(len(self.datos)):
            capaActual = []
            for columnas in range(len(self.datos[capas][0])):
                sumaColumna = 0
                for filas in range(len(self.datos[capas])):
                    sumaColumna += self.datos[capas][filas][columnas]
                capaActual.append(sumaColumna)
            resultado.append(capaActual)
        return resultado

    def verBorde(self):
        capa = self.datos
        numFilas = len(capa)
        numCol = len(capa[0])
        arregloDosDim = []
        posiciones = []
        for columnas in range(numCol):
            arregloDosDim.append(capa[0][columnas])
            posiciones.append((0, columnas))
        for filas in range(1, numFilas):
            arregloDosDim.append(capa[filas][numCol - 1])
            posiciones.append((filas, numCol - 1))
        for columnas in range(numCol - 2, -1, -1):
            arregloDosDim.append(capa[numFilas - 1][columnas])
            posiciones.append((numFilas - 1, columnas))
        for filas in range(numFilas - 2, 0, -1):
            arregloDosDim.append(capa[filas][0])
            posiciones.append((filas, 0))

        print("Arreglo: ", arregloDosDim)
        print("Posiciones: ", posiciones)
        return arregloDosDim

   

