import random
import copy
import population_structure as ps
import ui

def list_sucessors(placa):
    sucessores = []
    for i in range(0, len(placa.items)):
        sucessores.append(new_sucessor(placa, 1, 0, i))
        sucessores.append(new_sucessor(placa, -1, 0, i))
        sucessores.append(new_sucessor(placa, 0, 1, i))
        sucessores.append(new_sucessor(placa, 0, -1, i))
    return sucessores


def new_sucessor(placa, dx, dy, item):
    sucessor = copy.deepcopy(placa)
    sucessor.items[item].move(dx, dy)
    sucessor.generate_representation()
    sucessor.calculate_heuristic()
    return sucessor


def find_best(sucessores):
    min = sucessores[0].heuristic
    for x in sucessores:
        if x.heuristic <= min:
            melhor = x
            min = melhor.heuristic

    return melhor





def main():
    objects = [[3, 3], [5, 5], [4, 3], [6, 7], [1,8]]

    placa = ps.Set(20, 20, objects)
    print(placa)
    while(True):
        sucessores = list_sucessors(placa)
        melhor = find_best(sucessores)
        ui.print_set(melhor)
        if (placa.heuristic > melhor.heuristic):
            placa = melhor
        else:
            break

    ui.print_div('BEST ITERATION')
    ui.print_set(placa)

main()
