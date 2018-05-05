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
      self.items.append(Object(self.length, self.width, request))

    self.representation = concat_objects(
      self.length, self.width, self.items)
    self.fitness = 0

  def __str__(self):
    to_print = ''
    for line in self.representation:
      for position in line:
        to_print += str(position)
      to_print += '\n'
    return to_print


class Object:
  def __init__(self, grid_lenght, grid_width, request):
    if 0.5 > random.random():
      self.length = request[0]
      self.width = request[1]
    else:
      self.length = request[1]
      self.width = request[0]

    self.grid = init_grid(grid_length, grid_width)

    x = random.randint(0, grid_width - self.width - 1)
    y = random.randint(0, grid_length - self.length - 1)

    self.grid = positioning_object(
      self.grid, self.length, self.width, x, y)

  def __str__(self):
    to_print = ''
    for line in self.grid:
      for position in line:
        to_print += str(position)
      to_print += '\n'
    return to_print

# initialize a grid with given sizes


def init_grid(g_length, g_width):
  return[[0 for x in range(g_length)] for y in range(g_width)]


def positioning_object(grid, length, width, x, y):
  for i in range(x, x + width):
    for j in range(y, y + length):
      grid[i][j] = 1
  return grid

# concatenate the grids


def concat_objects(grid_lenght, grid_width, items):
  concated_grid = items[0].grid

  for i in range(1, len(items)):
    for j in range(grid_lenght):
      for k in range(grid_width):
        concated_grid[j][k] += items[i].grid[j][k]

  return concated_grid
