import ui
import population_structure as ps

def main(grid_height, grid_width, requested_objects):
  set = ps.Set(grid_height, grid_width, requested_objects, False)
  set.shuffle()
  set.place_objects()
  ui.print_div("FINAL")
  ui.print_set(set)