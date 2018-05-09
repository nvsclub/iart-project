import random
import copy

class Set:
  def __init__(self, grid_height, grid_width, requested_objects):
    self.items = []
    self.height = grid_height
    self.width = grid_width

    for request in requested_objects:
      self.items.append(Object(self, request))

    self.generate_representation()
    self.calculate_heuristic()

  def __str__(self):
    to_print = ''
    for line in self.representation:
      for position in line:
        to_print += str(position) + ' '
      to_print += '\n'
    return to_print

  def generate_representation(self):
    self.representation = copy.deepcopy(self.items[0].grid)

    for i in range(1, len(self.items)):
      for j in range(self.height):
        for k in range(self.width):
          self.representation[j][k] += self.items[i].grid[j][k]
  
  def calculate_heuristic(self):
    self.heuristic = 0
    for y in range(self.height):
      line_val = 5
      for x in range(self.width):
        if self.representation[y][x] > 1:
          self.heuristic += -(self.representation[y][x] ** 12)
        if self.representation[y][x] == 1:
          self.heuristic += 2 ** (self.height - y)
          line_val *= 2
        if self.representation[y][x] == 0 and line_val > 2:
          self.heuristic += line_val
          line_val = 2

    for x in range(self.width):
      col_val = 5
      for y in range(self.height):
        if self.representation[y][x] == 1:
          col_val *= 2
          self.heuristic += 2 ** (self.width - x)
        if self.representation[y][x] == 0 and line_val > 2:
          self.heuristic += col_val
          col_val = 2



class Object:
  def __init__(self, set, position):
    self.set = set

    if 0.5 > random.random():
      self.height = position[0]
      self.width = position[1]
    else:
      self.height = position[1]
      self.width = position[0]

    self.x = random.randint(0, self.set.width - self.width - 1)
    self.y = random.randint(0, self.set.height - self.height - 1)

    self.generate_grid()

  def __str__(self):
    to_print = ''
    for line in self.grid:
      for position in line:
        to_print += str(position) + ' '
      to_print += '\n'
    return to_print

  def generate_grid(self):
    self.grid = [[0 for i in range(self.set.width)] for j in range(self.set.height)]

    for i in range(self.y, self.y + self.height):
      for j in range(self.x, self.x + self.width):
        self.grid[i][j] = 1
        
  def move(self, dx, dy):
    if dx + self.x + self.width - 1 >= self.set.width or dy + self.y + self.height - 1 >= self.set.height or dx + self.x < 0 or dy + self.y < 0:
      return 
    else:
      self.x += dx
      self.y += dy
      self.generate_grid()
      
  # falta rodar sobre varios eixos
  def rotate(self):
    if self.x + self.height >= self.set.width or self.y + self.width >= self.set.height:
      return
    else:
      self.width, self.height = self.height, self.width
      self.generate_grid()