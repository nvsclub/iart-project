import random
import copy

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
    for successor in successors:
        if successor.heuristic < best.heuristic:
            best = successor

    return best

def main(grid_height, grid_width, requested_objects):
    state = ps.Set(grid_height, grid_width, requested_objects, True)
    state.shuffle()
    while(True):
        best = find_best(list_successors(state))
        if (state.heuristic > best.heuristic):
            state = best
            ui.print_set(state)
        else:
            break

    return state

