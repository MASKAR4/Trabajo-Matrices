class DatosDim1():
    def __init__(self, n, valorDefecto):
        self.datos = []
        for i in range(n):
            self.datos.append(valorDefecto)

    def ver(self):
        i = 0
        for item in self.datos:
            print(f'[{i}] {item} \t', end='')
            i += 1
