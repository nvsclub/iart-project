import random
import copy

class Set:
  def __init__(self, grid_height, grid_width, requested_objects, is_random):
    self.items = []
    self.height = grid_height
    self.width = grid_width
    self.heuristic = 1#(grid_width+1)*(grid_height+1)+(grid_width+1)+(grid_height+1)

    for i in range(len(requested_objects)):
      self.items.append(Object(self, i, requested_objects[i], is_random))

    self.generate_representation()

  def __str__(self):
    to_print = ''
    for line in self.representation:
      for position in line:
        to_print += str(position) + ' '
      to_print += '\n'
    return to_print

  def shuffle(self):
    random.shuffle(self.items)

  def generate_representation(self):
    self.representation = [[0 for i in range(self.width)] for j in range(self.height)]

    for i in range(0, len(self.items)):
      if self.items[i].grid == None:
        continue
      for j in range(self.height):
        for k in range(self.width):
          self.representation[j][k] += self.items[i].grid[j][k]
    
  def representation_reset(self):
    self.representation = [[0 for i in range(self.width)] for j in range(self.height)]
    for item in self.items:
      item.grid = None
  
  def calculate_old_heuristic(self):
    self.heuristic = 0
    for y in range(self.height):
      line_val = 5
      for x in range(self.width):
        if self.representation[y][x] > 1:
          self.heuristic += -(self.representation[y][x] ** 5)
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

  def calculate_heuristic(self, bestHeuristic):
    self.heuristic = bestHeuristic

    for y in range(self.height):
      consecutive_zeros = 0
      for x in range(self.width):
        if self.representation[y][x] == 0:
          consecutive_zeros += 1
        if self.representation[y][x] == 1 and consecutive_zeros > 0:
          self.heuristic += consecutive_zeros
          consecutive_zeros = 0
 
    for x in range(self.height):
      consecutive_zeros = 0
      for y in range(self.width):
        if self.representation[y][x] == 0:
          consecutive_zeros += 1
        if self.representation[y][x] == 1 and consecutive_zeros > 0:
          self.heuristic += consecutive_zeros
          consecutive_zeros = 0

  def place_objects(self):
    self.representation_reset()
    for item in self.items:
      pivot_points = self.get_pivot_points()

      best_heuristic, best_pivot, rotate = self.best_scenario(item, pivot_points)

      if best_heuristic == -1:
        return -1

      item.place(best_pivot[0], best_pivot[1], rotate)
      
      self.generate_representation()

    self.calculate_heuristic(best_heuristic)
    
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

  def best_scenario(self, item, pivot_points):
    heuristic_list = []
    pivot_no = -1
    best_heuristic = (self.width+1) * (self.height+1) + (self.width+1) + (self.height+1)
    for pivot in pivot_points:
      new_representation = copy.deepcopy(self.representation)
      if pivot[0] + item.width <= self.width and pivot[1] + item.height <= self.height:
        for x in range(pivot[0], pivot[0] + item.width):
          for y in range(pivot[1], pivot[1] + item.height):
            new_representation[y][x] += 1
        placement1 = self.case_heuristic(new_representation, self.width, self.height)
      else:
        placement1 = (self.width+1) * (self.height+1) + (self.width+1) + (self.height+1)
      heuristic_list.append(placement1) 

      new_representation = copy.deepcopy(self.representation)
      if pivot[0] + item.height <= self.width and pivot[1] + item.width <= self.height:
        for x in range(pivot[0], pivot[0] + item.height):
          for y in range(pivot[1], pivot[1] + item.width):
            new_representation[y][x] += 1
        placement2 = self.case_heuristic(new_representation, self.width, self.height)
      else:
        placement2 = (self.width+1) * (self.height+1) + (self.width+1) + (self.height+1)
      heuristic_list.append(placement2)

    i = 0
    for heuristic in heuristic_list:
      if heuristic < best_heuristic:  
        best_heuristic = heuristic
        pivot_no = i
      i += 1

    # print(heuristic_list)

    if pivot_no == -1:
      return -1, -1, False

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

    return max_used_height * max_used_width + max_used_height + max_used_width + bias_sobreposition


class Object:
  def __init__(self, set, id, size, is_random):
    self.set = set

    self.height = size[1]
    self.width = size[0]

    self.id = id

    if is_random:
      self.x = random.randint(0, self.set.width - self.width - 1)
      self.y = random.randint(0, self.set.height - self.height - 1)
    else:
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

  def __eq__(self, other):
    return self.id == other.id

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
      a = self.width
      self.width = self.height
      self.height = a

      self.y = self.y - self.width + 1
      
      self.generate_grid()
