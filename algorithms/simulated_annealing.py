import random
import copy
import math

def new_successor(state):
    sucessor = copy.deepcopy(state)
    item_1 = random.randint(0, len(state.items) - 1)
    while True:
        item_2 = random.randint(0, len(state.items) - 1)
        if not item_1 == item_2:
            break

    sucessor.items[item_2], sucessor.items[item_1] = sucessor.items[item_1], sucessor.items[item_2]
    sucessor.place_objects()
    return sucessor

def main(grid_height, grid_width, requested_objects):
    temperature = grid_height * grid_width
    state = ps.State(grid_height, grid_width, requested_objects, False)
    state.shuffle()
    state.place_objects()

    ui.print_state(state)
    ui.print_tooltip('Temperature: %d' % temperature)

    while temperature > 0:
        next_state = new_successor(state)
        delta_e = state.heuristic - next_state.heuristic 

        if delta_e > 0:
            state = next_state
            ui.print_state(state)
            ui.print_tooltip('Temperature: %d' % temperature)
        elif random.random() < math.exp(delta_e / temperature):
            state = next_state
            ui.print_state(state)
            ui.print_tooltip('Temperature: %d' % temperature)

        temperature -= 1
    
    ui.print_state(state)
    ui.print_tooltip('Temperature: %d' % temperature)
    return state




