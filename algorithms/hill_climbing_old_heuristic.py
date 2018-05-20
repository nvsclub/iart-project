import random
import copy

def list_successors(state):
    successors = []
    for i in range(0, len(state.items)):
        successors.append(new_successor(state, 1, 0, i))
        successors.append(new_successor(state, -1, 0, i))
        successors.append(new_successor(state, 0, 1, i))
        successors.append(new_successor(state, 0, -1, i))
        successors.append(new_successor_rotate(state, i))
    return successors


def new_successor(state, dx, dy, item):
    successor = copy.deepcopy(state)
    successor.items[item].move(dx, dy)
    successor.generate_representation()
    successor.calculate_old_heuristic()
    return successor

def new_successor_rotate(state, item):
    successor = copy.deepcopy(state)
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
    state = ps.State(grid_height, grid_width, requested_objects, True)
    state.shuffle()
    while(True):
        best = find_best(list_successors(state))
        if (state.heuristic > best.heuristic):
            state = best
            ui.print_state(state)
        else:
            break

    return state

