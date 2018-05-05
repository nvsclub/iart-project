import random
import copy
import population_structure as ps

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


    objects = [[3, 3], [3, 3], [3, 3]]

    placa = ps.Set(10, 10, objects)
    print(placa)
    while(True):
        print('##########################################################\n')
        sucessores = list_sucessors(placa)
        for x in sucessores:
            print(x)
            print(str(x.heuristic) + "\n")
        melhor = find_best(sucessores)
        if (placa.heuristic > melhor.heuristic):
            placa = melhor
        else:
            break

    print('########################## BEST ##########################\n')
    print(placa)
    print(str(placa.heuristic) + "\n")

main()
