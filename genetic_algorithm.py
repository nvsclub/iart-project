import random
import copy

import population_structure as ps
import ui

# define
population_size = 10
limit_of_generations = 1000
fitness_limit = 5000
no_stable_generations = 50

elitist_rate = 0.1
survival_rate = 0.7
mutation_rate = 0.2

def fitness_and_placement(population):
    for individual in population:
        individual.place_objects()
    return population


def selection(population):
    population = sorted(population, key=lambda individual: individual.heuristic, reverse=False)
    
    i = 0
    for _ in population:
        if i > elitist_rate*population_size:
            if random.random() > survival_rate/i:
                del population[i]
        i += 1
    return population

def crossover(population):
    while len(population) < population_size:
        parent1 = random.randint(0, len(population)-1)
        parent2 = random.randint(0, len(population)-1)

        individual = copy.deepcopy(population[parent1])

        crossover_point = random.randint(0, len(population[parent2].items))
        individual.items[:crossover_point]

        for item_in_parent in population[parent1].items:
            if item_in_parent in individual.items:
                continue
            else:
                individual.items.append(copy.deepcopy(item_in_parent))

        population.append(individual)

    return population

def mutation(population):
        i = 0
        for individual in population:
                if i > elitist_rate * population_size:
                        swap_random_elements(individual)
                        swap_random_elements(individual)
                        swap_random_elements(individual)
                i += 1
        return population

def swap_random_elements(individual):
        element_1 = random.randint(0, len(individual.items) - 1)
        element_2 = random.randint(0, len(individual.items) - 1)
        individual.items[element_1], individual.items[element_2] = individual.items[element_2], individual.items[element_1]


def main(grid_height, grid_width, items):

    # population initialization
    population = []
    stable_point = 0
    stable_generation = 0
    best = 99999
    for _ in range(population_size):
        individual = ps.Set(grid_height, grid_width, items, False)
        individual.shuffle()
        population.append(individual)

    # run though generations
    for generation in range(limit_of_generations):
        # refresh population fitnesses and representations
        fitness_and_placement(population)

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

        # calculate next generation
        population = selection(population)
        population = crossover(population)
        population = mutation(population)

    return population[0]

