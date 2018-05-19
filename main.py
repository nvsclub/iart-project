import population_structure as ps
import hill_climbing_old_heuristic
import hill_climbing_new_heuristic
import genetic_algorithm
import simulated_annealing
import random_algorythm
import sys
import time
import ui

def main():
    if len(sys.argv) == 2:
        choose_algorythm(read_file(sys.argv[1]))
        return
    elif len(sys.argv) == 3:
        start = time.time()
        result = run_algorithm(sys.argv[2], read_file(sys.argv[1]))
        
        end = time.time()
        ui.print_objects(result)
        ui.print_tooltip('Ellapsed time: %.2f seconds' % (end - start))
        return

    option = print_main_menu()

    if len(option) > 2:
        main()
    if '1' in option:
        read_data()
    elif '2' in option:
        create_data()
    elif '3' in option:
        input_data()
    else:
        main()

def read_data():
    print('Files should be placed in files folder, and be of type txt')
    choose_algorythm(read_file(input('Name of the file to read? ')))

def read_file(file_name):
    filepath = 'files/' + file_name + '.txt'
    data = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            data.append([int(i) for i in line.strip().split(' ')])
            line = fp.readline()
    return data

def create_data():
    print('The file will be created in the files folder')
    filepath = 'files/' + input('Name of the file? ') + '.txt'
    data = get_user_data()
    with open(filepath, 'w') as fp:
        for d in data:
            fp.write('%d %d\n' % (d[0], d[1]))

    choose_algorythm(data)

def input_data():
    choose_algorythm(get_user_data())

def validate_data(data):
        area = 0
        for i in range(1, len(data)):
                if data[i][0] > data[0][0] or data[i][1] > data[0][0] or data[i][1] > data[0][0] or data[i][0] > data[0][1]:
                        return False
                area += data[i][0] * data[i][1]

        return not area > data[0][0] * data[0][1]

def get_user_data():
    data = []
    board = []
    board.append(int(input('Board x size? ')))
    board.append(int(input('Board y size? ')))
    data.append(board)
    n = int(input('Number of objects? '))
    for i in range(1, n + 1):
        obj = []
        obj.append(int(input('Object #%d x size? ' % i)))
        obj.append(int(input('Object #%d y size? ' % i)))
        data.append(obj)
    return data

def choose_algorythm(data):
    if not validate_data(data):
        print('Error in data')
        return
    option = print_choose_algorythm()
    if len(option) > 2:
        print('Invalid option')
        choose_algorythm(data)

    start = time.time()
    
    result = run_algorithm(option, data)
    
    end = time.time()
    ui.print_objects(result)
    ui.print_tooltip('Ellapsed time: %.2f seconds' % (end - start))

def run_algorithm(option, data):
    if '1' in option:
        return hill_climbing_old_heuristic.main(data[0][0], data[0][1], data[1::])
    elif '2' in option:
        return hill_climbing_new_heuristic.main(data[0][0], data[0][1], data[1::])
    elif '3' in option:
        return simulated_annealing.main(data[0][0], data[0][1], data[1::])
    elif '4' in option:
        return genetic_algorithm.main(data[0][0], data[0][1], data[1::])
    elif '5' in option:
        return random_algorythm.main(data[0][0], data[0][1], data[1::])
    else:
        print('Invalid option')
        choose_algorythm(data)

def print_choose_algorythm():
    print('Select option:')
    print('    1. Hill Climbing (old heuristic)')
    print('    2. Hill Climbing (new heuristic)')
    print('    3. Simulated Annealing')
    print('    4. Genetic Algorithm')
    print('    5. Random')
    return input()

def print_main_menu():
    print('            IART v0.1\n')
    print('Select option:')
    print('    1. Read data from file')
    print('    2. Create data file')
    print('    3. Input manual data')
    return input()

if __name__ == "__main__":
    main()