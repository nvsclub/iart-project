import random
import population_structure as ps
import copy

# define
grid_height = 10
grid_width = 10

population_size = 20
limit_of_generations = 1000
fitness_limit = 0

elitist_rate = 0.2
survival_rate = 0.1
mutation_rate = 0.01

def minimum_sizes(objects, grid_height, grid_width):
  total_area = 0
  for o in objects:
    total_area += o[0] * o[1]
  
  return [round(total_area/grid_height+0.5), round(total_area/grid_width+0.5)]

def regenerate_representation(population):
  for individual in population:
    individual.generate_representation()

def refresh_fitness(population):
  for individual in population:
    individual.calculate_heuristic()

def selection(population):
  population = sorted(population, key=lambda individual: individual.heuristic, reverse=False)
  
  i = 0
  for individual in population:
    if i > elitist_rate*population_size:
      if random.random() > survival_rate:
        population.remove(individual)

def crossover(population):
  while len(population) < population_size:
    parent1 = random.randint(0, len(population))
    parent2 = random.randint(0, len(population))

    individual = copy.deepcopy(population[parent1])

    crossover_point = random.randint(0, len(population[parent2].objects))

    individual.objects = individual.objects[:crossover_point]

    for o in range(crossover_point, len(population[parent2].objects)):
      individual.objects = individual.objects + copy.deepcopy(population[parent2].objects[o])

def mutation(population):
  for individual in population:
    mutate(individual)
    
def mutate(individual):
  no_list = [-3, -2, -2, -1, -1, -1, 0, 1, 1, 1, 2, 2, 3]
  if random.random() < mutation_rate:
      dx = no_list[random.randint(0,len(no_list)-1)]
      dy = no_list[random.randint(0,len(no_list)-1)]
      chosen_object = random.randint(0, len(individual.objects)-1)
      if dx + individual.objects[chosen_object].x >= individual.objects[chosen_object].set.width or dy + individual.objects[chosen_object].y >= individual.objects[chosen_object].set.height or dx + individual.objects[chosen_object].x < 0 or dy + individual.objects[chosen_object].y < 0:
        pass
      else:
        individual.objects[chosen_object].move(dx, dy)
      return mutate(individual)
  
def print_population(population):
  for individual in population:
    print(individual)

def print_best(population):
  print(population[0])
  print(population[0].heuristic)

def main():
  # test objects
  objects = [[3,3],[3,3], [3,3]]

  # calculate minimum rows/columns
  [rows, columns] = minimum_sizes(objects, grid_height, grid_width)

  # population initialization
  population = []
  for _ in range(population_size):
    individual = ps.Set(grid_height, grid_width, objects, rows, columns)
    population.append(individual)



  # run though generations
  for generation in range(limit_of_generations):
    regenerate_representation(population)
    refresh_fitness(population)

    if population[0].heuristic == fitness_limit:
      print_best(population)
      break

    selection(population)
    crossover(population)
    mutation(population)

  regenerate_representation(population)
  refresh_fitness(population)
  print_best(population)



main()
