import random
import copy
import population_structure as ps
import ui

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
    successor.calculate_old_heuristic()
    return successor

def new_successor_rotate(set, item):
    successor = copy.deepcopy(set)
    successor.items[item].rotate()
    successor.generate_representation()
    successor.calculate_old_heuristic()
    return successor

def find_best(successors):
    best = successors[0]
    ui.print_div("SUCCESSORS")
    for successor in successors:
        ui.print_set(successor)
        if successor.heuristic < best.heuristic:
            best = successor

    return best

def main(grid_height, grid_width, requested_objects):
    set = ps.Set(grid_height, grid_width, requested_objects, True)
    set.shuffle()
    while(True):
        best = find_best(list_successors(set))
        ui.print_set(best)
        if (set.heuristic > best.heuristic):
            set = best
        else:
            break

    ui.print_div('BEST ITERATION')
    ui.print_set(set)
