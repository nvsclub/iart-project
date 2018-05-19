import population_structure as ps 
import ui

# test objects
items = [[1,1], [3,3], [3,3], [3,3], [3,3], [3,3], [3,3], [3,3], [1,1], [7,1], [7,1], [7,1], [7,1], [7,1]]
grid_height = 10
grid_width = 10

individual = ps.Set(grid_height, grid_width, items, False)
individual.shuffle()

individual.place_objects()

ui.print_set(individual)