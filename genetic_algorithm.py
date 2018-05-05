import random
import population_structure as ps

# define
grid_length = 10
grid_width = 10

no_cycles = 0
max_fitness = 0


def main():


    objects = [[3,3],[2,4]]

    a = ps.Set(grid_length, grid_width, objects)
    '''
    print(a)
    a.items[0].move_object(6,6)
    a.generate_representation()
    print(a)'''



    for item in a.items:
      print(item)

main()
