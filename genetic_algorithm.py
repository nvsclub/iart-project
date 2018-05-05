import random
import population_structure as ps

# define
grid_length = 10
grid_width = 10

population_size = 20

def minimum_sizes(objects, grid_length, grid_width):
  total_area = 0
  for o in objects:
    total_area += o[0] * o[1]
  
  return [total_area/grid_length, total_area/grid_width]

def main():
  # test objects
  objects = [[3,3],[2,4], [1,2]]

  # population initialization
  population = []
  for _ in range(1, population_size):
    individual = ps.Set(grid_length, grid_width, objects)
    population.append(individual)

  # calculate minimum rows/columns
  [rows, columns] = minimum_sizes(objects, grid_length, grid_width)

  print(rows, columns)



main()
