from manipulators.initialization import init_matrix, clear_matrix
from manipulators.paiting import paint_pixel

def call_action(matrix, command, params):
    switcher = {
        'I': lambda: init_matrix(*list(map(int, params))),
        'C': lambda: clear_matrix(matrix),
        'L': lambda: paint_pixel(
            matrix,
            *list(map(int, params[:2])),
            tuple(params[2:])),
    }
    func  = switcher.get(command, lambda: None)
    return func()

def main():
    command = ''
    matrix = []
    while(command is not 'X'):
        user_input = input()
        matrix = call_action(
            matrix,
            user_input.split()[0],
            user_input.split()[1:])

if __name__ == '__main__':
    main()