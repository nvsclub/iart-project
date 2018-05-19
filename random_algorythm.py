import ui
import copy
import population_structure as ps

generations = 100

def main(grid_height, grid_width, requested_objects):
    best_set = ps.Set(grid_height, grid_width, requested_objects, False)
    best_set.shuffle()
    best_set.place_objects()
    for _ in range(generations):
        new_set = ps.Set(grid_height, grid_width, requested_objects, False)
        new_set.shuffle()
        new_set.place_objects()
        if new_set.heuristic < best_set.heuristic:
            best_set = new_set
            ui.print_set(best_set)

    ui.print_div("FINAL")
    ui.print_set(best_set)

    return best_set