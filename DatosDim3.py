class DatosDim3():
    def __init__(self, x, y, z, valorDefecto):
        self.datos = []
        for i in range(x):
            listaTmp = []
            for j in range(y):
                listaTmpTmp = []
                for k in range(z):
                    listaTmpTmp.append(valorDefecto)
                listaTmp.append(listaTmpTmp)
            self.datos.append(listaTmp)

    def ver(self):
        i = 0
        for itemI in self.datos:
            j = 0
            for itemJ in itemI:
                k = 0
                for itemK in itemJ:
                    print(f'[{i}][{j}][{k}] {itemK} \t', end='')
                    k += 1
                print()
                j += 1
            print()
            i += 1

    def sumar(self):
        acumular = 0
        for itemI in self.datos:
            for itemJ in itemI:
                for itemK in itemJ:
                    acumular = acumular + itemK
        # print(f'Suma: {acumular}')
        return acumular

    def cambiarValor(self, x, y, z, nuevoValor):
        try:
            self.datos[x][y][z] = nuevoValor
            print(f' datos[{x}][{y}][{z}]:{nuevoValor}  con Exito!')
        except:
            print(f' datos[{x}][{y}][{z}]:{nuevoValor}  ERROR!')

    def resta(self):
        acumular = 0
        for itemI in self.datos:
            for itemJ in itemI:
                for itemK in itemJ:
                    acumular = acumular - itemK
        return acumular

    def sumaXfilas(self):
        suma_filas = []
        for i in range(len(self.datos)):
            suma = 0
            for j in range(len(self.datos[i])):
                for k in range(len(self.datos[i][j])):
                    suma += self.datos[i][j][k]
            suma_filas.append(suma)
        return suma_filas

    def sumaXcolumnas(self):
        suma_columnas = []
        for j in range(len(self.datos[0])):
            suma = 0
            for i in range(len(self.datos)):
                for k in range(len(self.datos[i][j])):
                    suma += self.datos[i][j][k]
            suma_columnas.append(suma)
        return suma_columnas

    def sumaXcapas(self):
        suma_capas = []
        for k in range(len(self.datos[0][0])):
            suma = 0
            for i in range(len(self.datos)):
                for j in range(len(self.datos[i])):
                    suma += self.datos[i][j][k]
            suma_capas.append(suma)
        return suma_capas

    def verBorde(self):
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                for k in range(len(self.datos[i][j])):
                    if i == 0 or i == len(self.datos) - 1 or j == 0 or j == len(
                            self.datos[i]) - 1 or k == 0 or k == len(self.datos[i][j]) - 1:
                        print(f'[{i}][{j}][{k}] {self.datos[i][j][k]} \t', end='')
                    else:
                        print('\t', end='')
