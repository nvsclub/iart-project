import random

# define
grid_length = 10
grid_width = 10

no_cycles = 0
max_fitness = 0


class Individual:
  def __init__(self, grid_length, grid_width, requested_objects):
    self.items = []
    self.length = grid_length
    self.width = grid_width

    for request in requested_objects:
      self.items.append(Object(self, request))

    self.generate_representation()
    self.fitness = 0

  def __str__(self):
    to_print = ''
    for line in self.representation:
      for position in line:
        to_print += str(position)
      to_print += '\n'
    return to_print

  def generate_representation(self):
    self.representation = self.items[0].grid

    for i in range(1, len(self.items)):
      for j in range(self.length):
        for k in range(self.width):
          self.representation[j][k] += self.items[i].grid[j][k]


class Object:
  def __init__(self, grid, position):
    self.grid = grid

    if 0.5 > random.random():
      self.length = position[0]
      self.width = position[1]
    else:
      self.length = position[1]
      self.width = position[0]

    x = random.randint(0, self.grid.width - self.width - 1)
    y = random.randint(0, self.grid.length - self.length - 1)

    self.generate_grid(x, y)

  def __str__(self):
    to_print = ''
    for line in self.grid:
      for position in line:
        to_print += str(position)
      to_print += '\n'
    return to_print

  def generate_grid(self, x, y):
    self.grid = [[0 for x in range(self.grid.length)] for y in range(self.grid.width)]

    for i in range(x, x + self.width):
      for j in range(y, y + self.length):
        self.grid[i][j] = 1