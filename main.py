import population_structure as ps
import hill_climbing_algorithm

def main():
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
  filepath = 'files/' + input('Name of the file to read? ') + '.txt'
  data = []
  with open(filepath) as fp:
    line = fp.readline()
    while line:
      data.append([int(i) for i in line.strip().split(' ')])
      line = fp.readline()
  choose_algorythm(data)

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
  option = print_choose_algorythm()
  if len(option) > 2:
    print('Invalid option')
    choose_algorythm(data)
  if '1' in option:
    hill_climbing_algorithm.main(data_to_set(data))
  else:
    print('Invalid option')
    choose_algorythm(data)

def data_to_set(data):
  return ps.Set(data[0][0], data[0][1], data[1::])

def print_choose_algorythm():
  print('Select option:')
  print('    1. Hill Climbing (old heuristic)')
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