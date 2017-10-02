from manipulators.initialization import init_image, clear_image
from manipulators.paiting import \
    paint_pixel, paint_column, paint_line, paint_rectangle, paint_area


def call_action(image, command, params):
    switcher = {
        'I': lambda: init_image(*list(map(int, params))),
        'C': lambda: clear_image(image),
        'L': lambda: paint_pixel(
            image,
            *list(map(int, params[:2])),
            tuple(list(map(int, params[2:])))),
        'V': lambda: paint_column(
            image,
            *list(map(int, params[:3])),
            tuple(list(map(int, params[3:])))),
        'H': lambda: paint_line(
            image,
            *list(map(int, params[:3])),
            tuple(list(map(int, params[3:])))),
        'K': lambda: paint_rectangle(
            image,
            *list(map(int, params[:4])),
            tuple(list(map(int, params[4:])))),
        'F': lambda: paint_area(
            image,
            *list(map(int, params[:2])),
            tuple(list(map(int, params[2:])))),
    }
    func = switcher.get(command, lambda: None)
    return func()


def main():
    command = ''
    image = None
    while(command is not 'X'):
        user_input = input()
        command = user_input.split()[0]
        params = user_input.split()[1:]
        image = call_action(
            image,
            command.upper(),
            params)


if __name__ == '__main__':
    main()
