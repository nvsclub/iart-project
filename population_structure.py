import random
import copy
import sys


class Set:
    def __init__(self, grid_height, grid_width, requested_objects, is_random):
        self.items = []
        self.height = grid_height
        self.width = grid_width
        self.heuristic = sys.maxsize

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
        self.representation = [
            [0 for i in range(self.width)] for j in range(self.height)]
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

        for x in range(self.width):
            consecutive_zeros = 0
            for y in range(self.height):
                if self.representation[y][x] == 0:
                    consecutive_zeros += 1
                if self.representation[y][x] == 1 and consecutive_zeros > 0:
                    self.heuristic += consecutive_zeros
                    consecutive_zeros = 0

    def place_objects(self):
        self.representation_reset()
        for item in self.items:
            best_heuristic, best_pivot, rotate = self.best_scenario(item, self.get_pivot_points())

            if best_heuristic == sys.maxsize:
                self.calculate_heuristic(best_heuristic)
                return

            item.place(best_pivot[0], best_pivot[1], rotate)
            self.generate_representation()

        self.calculate_heuristic(best_heuristic)

        return

    def get_pivot_points(self):
        pivots = []
        last_has_one = True

        for y in range(self.height):
            first_zero = None
            has_one = False
            for x in range(self.width):
                if self.representation[y][x] == 0 and first_zero == None:
                    first_zero = [x, y]
                if self.representation[y][x] == 1 and not has_one:
                    has_one = True

            if last_has_one and not first_zero == None:
                pivots.append(first_zero)

            last_has_one = has_one

        return pivots

    def best_scenario(self, item, pivot_points):
        best_heuristic, best_pivot, rotate = sys.maxsize, None, False

        for pivot in pivot_points:
            pivot_heuristic, new_pivot = self.test_pivot(pivot, item.height, item.width)
            if pivot_heuristic < best_heuristic:
                best_heuristic = pivot_heuristic
                best_pivot = new_pivot
                rotate = False

            pivot_heuristic, new_pivot = self.test_pivot(pivot, item.width, item.height)
            if pivot_heuristic < best_heuristic:
                best_heuristic = pivot_heuristic
                best_pivot = new_pivot
                rotate = True

        return best_heuristic, best_pivot, rotate

    def test_pivot(self, pivot, height, width):
      representation = copy.deepcopy(self.representation)
      pivot_x, pivot_y = pivot[0], pivot[1]
      if pivot[0] + width > self.width or pivot[1] + height > self.height:
          pivot_x, pivot_y = 0, 0

      for x in range(pivot_x, pivot_x + width):
          for y in range(pivot_y, pivot_y + height):
              representation[y][x] += 1
      
      return self.case_heuristic(representation), [pivot_x, pivot_y]

    def case_heuristic(self, new_representation):
        max_used_width = self.width
        max_used_height = 0
        bias_sobreposition = 0
        for x in range(self.width):
            empty_column = True
            for y in range(self.height):
                if new_representation[y][x] == 1:
                    used_height = y
                    empty_column = False
                if new_representation[y][x] > 1:
                    bias_sobreposition = 2 * self.width * self.height
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
