import random
import copy

import population_structure as ps
import ui



# define
grid_height = 10
grid_width = 10

population_size = 50
limit_of_generations = 10000
fitness_limit = 5000
no_stable_generations = 1000

elitist_rate = 0.2
survival_rate = 0.3
mutation_rate = 0.2

def regenerate_representation(population):
  for individual in population:
    individual.generate_representation()
  return population

def refresh_fitness(population):
  for individual in population:
    individual.calculate_heuristic()
  return population

def selection(population):
  population = sorted(population, key=lambda individual: individual.heuristic, reverse=False)
  
  i = 0
  for individual in population:
    if i > elitist_rate*population_size:
      if random.random() > survival_rate/i:
        del population[i]
    i += 1
  return population

def crossover(population):
  while len(population) < population_size:
    parent1 = random.randint(0, len(population)-1)
    #parent2 = random.randint(0, len(population))

    individual = copy.deepcopy(population[parent1])

    population.append(individual)

    #crossover_point = random.randint(0, len(population[parent2].items))

    #individual.items = individual.items[:crossover_point]

    #for o in range(crossover_point, len(population[parent2].items)):
    #  individual.items.append(copy.deepcopy(population[parent2].items[o]))

    return population

def mutation(population):
  i=0
  for individual in population:
    if i > elitist_rate*population_size:
      mutate(individual)
    i+=1
  return population
    
def mutate(individual):
  # list possible mutations and their frequency
  # #no_list = [-3, -2, -2, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 2, 2, 3]
  no_list = [-1, 1]
  if random.random() < mutation_rate:
      # generate a random object from the list (items) to mutate
      chosen_object = random.randint(0, len(individual.items)-1)

      # if there is a mutation choose a random mutation direction or a rotational one
      # # x direction
      if random.random() < 0.33:
        dx = no_list[random.randint(0,len(no_list)-1)]
        dy = 0
        individual.items[chosen_object].move(dx, dy)
      # # y direction
      elif random.random() < 0.66:
        dy = no_list[random.randint(0,len(no_list)-1)]
        dx = 0
        individual.items[chosen_object].move(dx, dy)
      # # rotation on the top left vertice
      else:
        individual.items[chosen_object].rotate()

      return mutate(individual)

def main():
  # test objects
  items = [[3,1], [3,1], [3,1], [3,1], [3,1], [3,1], [3,1], [3,1], [3,1], [3,1]]

  # population initialization
  population = []
  stable_point = 0
  best = 99999
  for _ in range(population_size):
    individual = ps.Set(grid_height, grid_width, items)
    population.append(individual)

  # run though generations
  for generation in range(limit_of_generations):
    # refresh population fitnesses and representations
    regenerate_representation(population)
    refresh_fitness(population)

    # ui interface
    if population[0].heuristic < best:
      best = population[0].heuristic
      ui.print_set(population[0])

    # exiting clauses
    # # stabilization arround a certain heuristic
    if population[0].heuristic != stable_point:
      stable_point = population[0].heuristic
      stable_generation = generation
    if generation - stable_generation >= no_stable_generations:
      break

    # # hitting the fitness limit # obsolete
    '''if population[0].heuristic <= fitness_limit:
      break'''

    # calculate next generation
    population = selection(population)
    population = crossover(population)
    population = mutation(population)


main()
