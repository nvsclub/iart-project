import random
import copy
import population_structure as ps
import ui
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
    state = ps.Set(grid_height, grid_width, requested_objects, False)
    state.shuffle()
    state.place_objects()

    ui.print_div("INICIAL")
    ui.print_set(state)
    ui.print_tooltip('Temperature: %.1f' % temperature)

    while temperature > 0:
        next_state = new_successor(state)
        delta_e = state.heuristic - next_state.heuristic 

        print('exp: %.2f' % -(delta_e / temperature))

        if delta_e > 0:
            state = next_state
            ui.print_set(state)
            ui.print_tooltip('Temperature: %.1f' % temperature)
        elif random.random() < math.exp(delta_e / temperature):
            state = next_state
            ui.print_set(state)
            ui.print_tooltip('Temperature: %.1f' % temperature)

        temperature -= 1
    
    ui.print_div("FINAL")
    ui.print_set(state)
    return state




