import term

def print_grid(grid):
    print_bundle = ''
    n_to_center = center_element(len(grid[0]) * 2) 
    for line in grid:
        print_bundle += (' ' * n_to_center)
        for i in range(len(line)):
            if line[i] == 0:
                print_bundle += term.black + term.bgyellow +'%d ' % line[i] + term.off
            elif line[i] == 1:
                print_bundle += term.black + term.bggreen + '%d ' % line[i] + term.off
            elif line[i] > 1:
                print_bundle += term.black + term.bgred + '%d ' % line[i] + term.off
        if i < len(line):
            print_bundle += '\n'
    
    term.write(print_bundle)

def print_objects(state):
    grid = [[0 for i in range(state.width)] for j in range(state.height)]
    for item in state.items:
        for i in range(item.y, item.y + item.height):
            for j in range(item.x, item.x + item.width):
                if grid[i][j] == 0:
                    grid[i][j] = item.id + 1
                else:
                    if type(grid[i][j]) is list or grid[i][j] == None:
                        grid[i][j] = None
                    else:
                        grid[i][j] = [grid[i][j], item.id + 1]

    print_bundle = ''
    n_to_center = center_element(len(grid[0]) * 2) 
    for line in grid:
        print_bundle += (' ' * n_to_center)
        for i in range(len(line)):
            if line[i] == 0:
                print_bundle += term.black + term.bgyellow + '0 ' + term.off
            elif type(line[i]) is list:
                print_bundle += term.black + term.bgred + '%c%c' % (chr(64 + line[i][0]), chr(64 + line[i][1])) + term.off
            elif line[i] == None:
                print_bundle += term.black + term.bgred + '--' + term.off
            else:
                print_bundle += term.black + term.bggreen +'%c ' % (chr(64 + line[i])) + term.off
        if i < len(line):
            print_bundle += '\n'
    
    term.write(print_bundle)

def print_state(state):
    print_grid(state.representation)
    print_tooltip('Heuristic: %d' % state.heuristic)

def print_tooltip(string):
    term.write( term.bgblue + string + term.off + '\n')

def center_element(size):
    return int((term.getSize()[1] - size) / 2)

def print_div(string):
    n_to_center = center_element(len(string))
    term.write(term.bgblue + '\n' + (' ' * n_to_center) + string + (' ' * n_to_center) + term.off + '\n')
