def print_grid(grid):
    print_bundle = '' 
    for line in grid:
        for i in range(len(line)):
                print_bundle += '%d ' % line[i]
        if(i < len(line)):
            print_bundle += '\n'
    
    print(print_bundle)

def print_set(set):
    print_grid(set.representation)
    print('Heuristic: %d\n' % set.heuristic)

def print_div(string):
    print('########## ' + string + ' ##########\n')
