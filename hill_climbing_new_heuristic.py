import random
import copy
import population_structure as ps
import ui_windows as ui


def list_successors(set):
    successors = []
    for i in range(0, len(set.items)):
        successors.append(new_successor(set, 1, 0, i))
        successors.append(new_successor(set, -1, 0, i))
        successors.append(new_successor(set, 0, 1, i))
        successors.append(new_successor(set, 0, -1, i))
        successors.append(new_successor_rotate(set, i))
    return successors

def new_successor(set, dx, dy, item):
    successor = copy.deepcopy(set)
    successor.items[item].move(dx, dy)
    successor.generate_representation()
    successor.calculate_heuristic()
    return successor


def main(grid_height, grid_width, requested_objects):
    set = ps.Set(grid_height, grid_width, requested_objects, False)
    set.place_objects()
    set.generate_representation()
    ui.print_set(set)
    '''while(True):
        successors = list_successors(set)
        best = find_best(successors)
        ui.print_set(best)
        if (set.heuristic < best.heuristic):
            set = best
        else:
            break'''
