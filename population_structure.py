import random
import copy
import ui

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
    self.representation = [[0 for i in range(self.width)] for j in range(self.height)]

    for i in range(0, len(self.items)):
      if self.items[i].grid == None:
        continue
      for j in range(self.height):
        for k in range(self.width):
          self.representation[j][k] += self.items[i].grid[j][k]
  
  def calculate_heuristic(self):
    self.heuristic = 0

    for y in range(self.height):
      for x in range(self.width):
        if self.representation[y][x] > 1: # Adds per overlap space
          self.heuristic += self.representation[y][x] * self.width * self.height

        if self.representation[y][x] == 1:
          self.heuristic += x + y * self.width 

  def place_objects(self):
    for item in self.items:
      pivot_points = self.get_pivot_points()

      print(pivot_points)

      best_heuristic, best_pivot, rotate = self.best_scenario(self, item, pivot_points)

      item.place(best_pivot[0], best_pivot[1], rotate)
      
      self.generate_representation()
      self.heuristic = best_heuristic
      ui.print_set(self)

    return

  def get_pivot_points(self):
    pivots = []
    disable_pivot = False

    last_has_one = True
    for y in range(self.height):
      first_zero = None
      has_one = False
      for x in range(self.width):
        if self.representation[y][x] == 0 and first_zero == None:
          first_zero = [x,y]
        if self.representation[y][x] == 1 and not has_one:
          has_one = True
        
      if last_has_one and not first_zero == None:
        pivots.append(first_zero)

      last_has_one = has_one
    
    return pivots

  def best_scenario(self, set, item, pivot_points):
    heuristic_list = []
    best_heuristic = set.width * set.height
    for pivot in pivot_points:
      new_representation = copy.deepcopy(set.representation)
      if pivot[0] + item.width <= set.width and pivot[1] + item.height <= set.height:
        for x in range(pivot[0], pivot[0] + item.width):
          for y in range(pivot[1], pivot[1] + item.height):
            new_representation[y][x] += 1
        placement1 = self.case_heuristic(new_representation, set.width, set.height)
      else:
        placement1 = best_heuristic
      heuristic_list.append(placement1) 

      new_representation = copy.deepcopy(set.representation)
      if pivot[0] + item.height <= set.width and pivot[1] + item.width <= set.height:
        for x in range(pivot[0], pivot[0] + item.height):
          for y in range(pivot[1], pivot[1] + item.width):
            new_representation[y][x] += 1
        placement2 = self.case_heuristic(new_representation, set.width, set.height)
      else:
        placement2 = best_heuristic
      heuristic_list.append(placement2)

    i = 0
    for heuristic in heuristic_list:
      if heuristic < best_heuristic:  
        best_heuristic = heuristic
        pivot_no = i
      i += 1

    if pivot_no % 2 == 1:
      return best_heuristic, pivot_points[int((pivot_no-1)/2)], True
    else:
      return best_heuristic, pivot_points[int((pivot_no)/2)], False

  def case_heuristic(self, new_representation, width, height):
    max_used_width = width
    max_used_height = 0
    bias_sobreposition = 0
    for x in range(width):
      empty_column = True
      for y in range(height):
        if new_representation[y][x] == 1:
          used_height = y
          empty_column = False
        if new_representation[y][x] > 1:
          bias_sobreposition = 2 * width * height
          empty_column = True
      if empty_column:
        max_used_width = x
        break
      if used_height > max_used_height:
        max_used_height = used_height
        
    max_used_height += 1
    max_used_width += 1

    return max_used_height * max_used_width + max_used_height + max_used_width + bias_sobreposition


class Object:
  def __init__(self, set, position):
    self.set = set

    self.height = position[1]
    self.width = position[0]

    self.x = None
    self.y = None

    self.generate_grid()

  def __str__(self):
    to_print = ''
    for line in self.grid:
      for position in line:
        to_print += str(position) + ' '
      to_print += '\n'
    return to_print

  def generate_grid(self):
    if self.x == None or self.y == None:
      self.grid = None
      return

    self.grid = [[0 for i in range(self.set.width)] for j in range(self.set.height)]
    for i in range(self.y, self.y + self.height):
      for j in range(self.x, self.x + self.width):
        self.grid[i][j] = 1

  def place(self, x, y, rotate):
    if rotate == True:
      self.width, self.height = self.height, self.width
    self.x = x
    self.y = y
    self.generate_grid()
    


  '''def move(self, dx, dy):
    if dx + self.x + self.width - 1 >= self.set.width or dy + self.y + self.height - 1 >= self.set.height or dx + self.x < 0 or dy + self.y < 0:
      return 
    else:
      self.x += dx
      self.y += dy
      self.generate_grid()
      
  # falta rodar sobre varios eixos
  def rotate(self):
    if self.x + self.height >= self.set.width or self.y + self.width >= self.set.height or self.y - self.height + 1 < 0:
      return
    else:
      a = self.width
      self.width = self.height
      self.height = a

      self.y = self.y - self.width + 1
      
      self.generate_grid()  '''