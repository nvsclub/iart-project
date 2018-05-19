import random
import copy
import population_structure as ps
import ui


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

def ciclo_hill_climbing(set):
    while (True):
        successors = list_successors(set)
        best = find_best(successors)
        if (set.heuristic > best.heuristic):
            set = best
        else:
            break
    return set

def main(grid_height, grid_width, requested_objects, arrefecimento):
    set = ps.Set(grid_height, grid_width, requested_objects, False)
    set.shuffle()
    set.place_objects()
    ui.print_div("INICIAL")
    ui.print_set(set)
    i = 0
    while i <= 50:
        set_aux = ciclo_hill_climbing(set)
        if i == 0:
            set_final = set_aux
        else:
            if set_aux.heuristic < set_final.heuristic:
                print("Encontrada nova solução:")
                set_final = set_aux
                ui.print_set(set_final)
                i = 0
        if arrefecimento == False:
            break
        set.shuffle()
        set.place_objects()
        i = i + 1

    ui.print_div("FINAL")
    ui.print_set(set_final)

    return set



