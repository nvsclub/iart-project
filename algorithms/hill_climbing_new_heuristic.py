import random
import copy

def list_successors(state):
    successors = []
    for i in range(0, len(state.items) - 1):
        for x in range(i + 1, len(state.items)):
            successors.append(new_successor(state,i,x))
    return successors

def new_successor(state, item_1, item_2):
    sucessor = copy.deepcopy(state)
    sucessor.items[item_2], sucessor.items[item_1] = sucessor.items[item_1], sucessor.items[item_2]
    sucessor.place_objects()
    return sucessor

def find_best(successors):
    best = successors[0]
    for successor in successors:
        if successor.heuristic <= best.heuristic:
            best = successor
    return best

def main(grid_height, grid_width, requested_objects):
    state = ps.State(grid_height, grid_width, requested_objects, False)
    state.shuffle()
    state.place_objects()
    while (True):
        best = find_best(list_successors(state))
        if (state.heuristic > best.heuristic):
            ui.print_state(state)
            state = best
        else:
            break

    ui.print_state(state)

    return state



