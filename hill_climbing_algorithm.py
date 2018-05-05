import random
import population_structure as ps

class item:
    def __init__(self, n, m, n_objeto, m_objeto):
        self.grid = [[0 for x in range(n)] for y in range(m)]
        self.x_i = random.randint(0, n - n_objeto)
        self.y_i = random.randint(0, m - m_objeto)
        for x  in range(self.x_i, self.x_i + n_objeto):
            for y in range(self.y_i, self.y_i + m_objeto):
                self.grid[x][y] = 1

    def __str__(self):
        to_print = ''
        for line in self.grid:
            for position in line:
                to_print += str(position)
            to_print += '\n'
        return to_print


class tabua:

    def __init__(self, n, m):
        tabua.n = n
        tabua.m = n
        self.grid = [[0 for x in range(n)] for y in range(m)]

    def __str__(self):
        to_print = ''
        for line in self.grid:
            for position in line:
                to_print += str(position)
            to_print += '\n'
        return to_print

    def adiciona_objetos(self, objs):
        for x in range(tabua.n):
            for y in range(tabua.m):
                for obj in self.objetos:
                    tabua.grid[x][y] += objs[obj].grid[x][y]


objetos = []

for x in range(0, 4):
    objetos.append(item(10, 10, 5, 5))
    print(objetos[x])

placa = tabua(10, 10)
placa.adiciona_objetos(objetos)


print(placa)
