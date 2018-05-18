import random
import copy
import population_structure as ps
import ui_windows as ui


def list_successors(set):
    successors = []
    for i in range(0, len(set.items) - 1):
        for x in range(i + 1, len(set.items)):
            successors.append(new_successor(set,i,x))
    return successors

def new_successor(set, item_1, item_2):
    sucessor = copy.deepcopy(set)
    sucessor.items[item_2], sucessor.items[item_1] = sucessor.items[item_1], sucessor.items[item_2]
    sucessor.place_objects()
    return sucessor

def find_best(successors):
    best = successors[0]
    ui.print_div('SUCCESSORS')
    for successor in successors:
        ui.print_set(successor)
        if successor.heuristic >= best.heuristic:
            best = successor
    return best

def main(grid_height, grid_width, requested_objects):
    set = ps.Set(grid_height, grid_width, requested_objects, False)
    set.place_objects()
    print("set inicial:")
    print("heuristica: " + str(set.heuristic))
    ui.print_set(set)
    while (True):
        successors = list_successors(set)
        best = find_best(successors)
        if (set.heuristic < best.heuristic):
            set = best
        else:
            break
    print("novo set: ")
    ui.print_set(set)
    print("heuristica: " + str(best.heuristic))
