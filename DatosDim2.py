class DatosDim2():
    def __init__(self, n, m, valorDefecto):
        self.datos = []
        for i in range(n):
            listaTmp = []
            for j in range(m):
                listaTmp.append(valorDefecto)
            self.datos.append(listaTmp)

    def ver(self):
        i = 0
        for itemI in self.datos:
            j = 0
            for itemJ in itemI:
                print(f'[{i}][{j}] {itemJ} \t', end='')
                j += 1
            print()
            i += 1
