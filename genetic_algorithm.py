import random
import copy

import population_structure as ps
import ui

# define
grid_height = 10
grid_width = 10

population_size = 1
limit_of_generations = 50
fitness_limit = 5000
no_stable_generations = 1000

elitist_rate = 0.2
survival_rate = 0.3
mutation_rate = 0.2

def fitness_and_placement(population):
  for individual in population:
    individual.place_objects()
    #if individual.place_objects() == -1:
      #print("Incompatible Solution")
  return population
'''
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
      element_1 = random.randint(0, len(individual.items)-1)
      element_2 = random.randint(0, len(individual.items)-1)
      individual.items[element_1], individual.items[element_2] = individual.items[element_2], individual.items[element_1]
    i+=1
  return population

'''
def main():
  # test objects
  items = [[2,2], [3,1], [2,1], [1,1], [2,1], [1,3], [2,1], [3,1]]

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
    fitness_and_placement(population)
    for i in range(population_size):
      ui.print_set(population[i])
  # ui interface
  '''if population[0].heuristic < best:
    best = population[0].heuristic
    ui.print_set(population[0])'''



  # exiting clauses
  # # stabilization arround a certain heuristic
  '''if population[0].heuristic != stable_point:
    stable_point = population[0].heuristic
    stable_generation = generation
  if generation - stable_generation >= no_stable_generations:
    break'''

  # calculate next generation
  #population = selection(population)
  #population = crossover(population)


main()
