import random
import copy

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
    for successor in successors:
        if successor.heuristic <= best.heuristic:
            best = successor
    return best

def hill_climbing(set):
    
    return set

def main(grid_height, grid_width, requested_objects):
    state = ps.Set(grid_height, grid_width, requested_objects, False)
    state.shuffle()
    state.place_objects()
    while (True):
        best = find_best(list_successors(state))
        if (state.heuristic > best.heuristic):
            ui.print_set(state)
            state = best
        else:
            break

    ui.print_set(state)

    return state



