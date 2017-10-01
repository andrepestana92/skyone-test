from manipulators.init_matrix import init_matrix

def call_action(command, params):
    switcher = {
        'I': lambda: init_matrix(*list(map(int, params)))
    }
    func  = switcher.get(command, lambda: None)
    return func()

def main():
    command = ''
    matrix = []
    while(command is not 'X'):
        user_input = input()
        command = user_input.split()[0]
        params = user_input.split()[1:]
        matrix = call_action(command, params)

if __name__ == '__main__':
    main()