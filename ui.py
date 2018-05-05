import term

def print_grid(grid):
    print_bundle = ''
    n_to_center = center_element(len(grid[0]) * 2) 
    for line in grid:
        print_bundle += (' ' * n_to_center)
        for i in range(len(line)):
            if(line[i] == 0):
                print_bundle += term.black + term.bgyellow +'%d ' % line[i] + term.off
            elif(line[i] == 1):
                print_bundle += term.black + term.bggreen + '%d ' % line[i] + term.off
            elif(line[i] > 1):
                print_bundle += term.black + term.bgred + '%d ' % line[i] + term.off
        if(i < len(line)):
            print_bundle += '\n'
    
    term.write(print_bundle)

def print_set(set):
    print_grid(set.representation)
    term.write( term.bgblue + 'Heuristic: %d' % set.heuristic + term.off + '\n')

def center_element(size):
    return int((term.getSize()[1] - size) / 2)

def print_div(string):
    n_to_center = center_element(len(string))
    term.write(term.bgblue + '\n' + (' ' * n_to_center) + string + (' ' * n_to_center) + term.off + '\n')
