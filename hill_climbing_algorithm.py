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
    successor.calculate_heuristic()
    return successor

def new_successor_rotate(set, item):
    successor = copy.deepcopy(set)
    successor.items[item].rotate()
    successor.generate_representation()
    successor.calculate_heuristic()
    return successor

def find_best(successors):
    best = successors[0]
    ui.print_div('SUCCESSORS')
    for successor in successors:
        ui.print_set(successor)
        if successor.heuristic >= best.heuristic:
            best = successor

    return best

def main():
    objects = [[3, 3], [3, 3], [4, 3], [2,5], [1,3]]

    set = ps.Set(10, 10, objects)
    while(True):
        successors = list_successors(set)
        best = find_best(successors)
        ui.print_set(best)
        if (set.heuristic < best.heuristic):
            set = best
        else:
            break

    ui.print_div('BEST ITERATION')
    ui.print_set(set)

main()
