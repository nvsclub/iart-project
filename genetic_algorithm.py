import random
import population_structure as ps

# define
grid_length = 10
grid_width = 10

no_cycles = 0
max_fitness = 0


def main():

    objects = [[1, 1], [4, 3], [1, 4]]

    a = ps.Individual(grid_length, grid_width, objects)

    # for item in a.items:
    #	print(item)

    print(a)


main()
