def print_grid(grid):
    print_bundle = '' 
    for line in grid:
        print_bundle += (' ' * 30)
        for i in range(len(line)):
                print_bundle += '%d ' % line[i]
        if(i < len(line)):
            print_bundle += '\n'
    
    print(print_bundle, end='')

def print_state(state):
    print_grid(state.representation)
    print_tooltip('Heuristic: %d' % state.heuristic)

def print_tooltip(string):
    print(string + '\n', end='')

def print_div(string):
    print('############################## ' + string + ' ##############################\n', end='')

def print_objects(individual):
    grid = [[0 for i in range(individual.width)] for j in range(individual.height)]
    for item in individual.items:
        for i in range(item.y, item.y + item.height):
            for j in range(item.x, item.x + item.width):
                if grid[i][j] == 0:
                    grid[i][j] = item.id + 1
                else:
                    if type(grid[i][j]) is list:
                        grid[i][j] = None
                    else:
                        grid[i][j] = [grid[i][j], item.id + 1]

    print_bundle = ''
    for line in grid:
        print_bundle += (' ' * 30)
        for i in range(len(line)):
            if line[i] == 0:
                print_bundle += '0 '
            elif type(line[i]) is list:
                print_bundle += '%c%c' % (chr(64 + line[i][0]), chr(64 + line[i][1]))
            elif line[i] == None:
                print_bundle += '--'
            else:
                print_bundle += '%c ' % (chr(64 + line[i]))
        if i < len(line):
            print_bundle += '\n'
    
    print(print_bundle, end="")