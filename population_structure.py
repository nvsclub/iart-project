import random
import copy

class Set:
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
    self.representation = copy.deepcopy(self.items[0].grid)

    for i in range(1, len(self.items)):
      for j in range(self.length):
        for k in range(self.width):
          self.representation[j][k] += self.items[i].grid[j][k]


class Object:
  def __init__(self, set, position):
    self.set = set

    if 0.5 > random.random():
      self.length = position[0]
      self.width = position[1]
    else:
      self.length = position[1]
      self.width = position[0]

    self.x = random.randint(0, self.set.width - self.width - 1)
    self.y = random.randint(0, self.set.length - self.length - 1)

    self.generate_grid()

  def __str__(self):
    to_print = ''
    for line in self.grid:
      for position in line:
        to_print += str(position)
      to_print += '\n'
    return to_print

  def generate_grid(self):
    self.grid = [[0 for i in range(self.set.length)] for j in range(self.set.width)]

    for i in range(self.y, self.y + self.width):
      for j in range(self.x, self.x + self.length):
        self.grid[i][j] = 1

  def move(self, dx, dy):
    if dx + self.x >= self.set.width or dy + self.y >= self.set.length or dx + self.x < 0 or dy + self.y < 0:
      return 
    else:
      self.x += dx
      self.y += dy
      self.generate_grid()
    