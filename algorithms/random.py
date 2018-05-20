import copy

generations = 1000

def main(grid_height, grid_width, requested_objects):
    state = ps.State(grid_height, grid_width, requested_objects, False)
    state.shuffle()
    state.place_objects()
    ui.print_state(state)
    for _ in range(generations):
        new_state = ps.State(grid_height, grid_width, requested_objects, False)
        new_state.shuffle()
        new_state.place_objects()
        if new_state.heuristic < state.heuristic:
            state = new_state
            ui.print_state(state)

    return state
