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
