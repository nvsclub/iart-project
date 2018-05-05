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
    for line in self.representation:
      usedLine = False
      lineCount = 0
      for position in line:
          if position != 0 and not usedLine: # Adds if line is used
            self.heuristic += 2
            usedLine = True
          
          if position == 0:
            lineCount += 1

          if position > 0 and lineCount > 0: # Adds per 0 gap in line
            self.heuristic += lineCount
            lineCount = 0
          
          if position > 1: # Adds per overlap space
            self.heuristic += position ** 2

    for x in range(self.width):
      columnCount = 0
      for y in range(self.height):
        if self.representation[y][x] == 0:
          columnCount += 1

        if self.representation[y][x] > 0 and columnCount > 0: # Adds per 0 gap in column
          self.heuristic += columnCount
          columnCount = 0



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
    self.grid = [[0 for i in range(self.set.height)] for j in range(self.set.width)]

    for i in range(self.y, self.y + self.height):
      for j in range(self.x, self.x + self.width):
        self.grid[i][j] = 1
        
  def move(self, dx, dy):
    if dx + self.x >= self.set.width or dy + self.y >= self.set.height or dx + self.x < 0 or dy + self.y < 0:
      return 
    else:
      self.x += dx
      self.y += dy
      self.generate_grid()
    