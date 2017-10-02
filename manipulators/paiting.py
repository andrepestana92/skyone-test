def paint_pixel(image, line, column, colour):
    if line >= 0 and line < image.size[1]\
            and column >= 0 and column < image.size[0]:
        pixels = image.load()
        pixels[column, line] = colour
    return image


def paint_column(image, line, first_column, last_column, colour):
    if line >= 0 and line < image.size[1]\
            and first_column >= 0 and last_column < image.size[0]:
        pixels = image.load()
        for j in range(first_column, last_column+1):
            pixels[j, line] = colour
    return image


def paint_line(image, first_line, last_line, column, colour):
    if column >= 0 and column < image.size[1]\
            and first_line >= 0 and last_line < image.size[0]:
        pixels = image.load()
        for i in range(first_line, last_line+1):
            pixels[column, i] = colour
    return image


def paint_rectangle(
        image,
        first_line,
        last_line,
        first_column,
        last_column,
        colour):
    for line in range(first_line, last_line+1):
        paint_column(image, line, first_column, last_column, colour)
    return image


def paint_area(image, line, column, colour):
    if line >= 0 and line < image.size[1]\
            and column >= 0 and column < image.size[0]:
        pixels = image.load()
        recursive_paint_area(
            pixels,
            line,
            column,
            image.size,
            colour,
            pixels[column, line],)
    return image


def recursive_paint_area(
        pixels,
        line,
        column,
        image_size,
        new_colour,
        original_colour):
    if line >= 0 and line < image_size[1]\
            and column >= 0 and column < image_size[0]:
        if pixels[column, line] == original_colour:
            pixels[column, line] = new_colour
            recursive_paint_area(
                pixels,
                line - 1,
                column,
                image_size,
                new_colour,
                original_colour)
            recursive_paint_area(
                pixels,
                line + 1,
                column,
                image_size,
                new_colour,
                original_colour)
            recursive_paint_area(
                pixels,
                line,
                column - 1,
                image_size,
                new_colour,
                original_colour)
            recursive_paint_area(
                pixels,
                line,
                column + 1,
                image_size,
                new_colour,
                original_colour)
