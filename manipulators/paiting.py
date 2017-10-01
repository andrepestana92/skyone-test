def paint_pixel(matrix, line, column, colour):
    try:
        matrix[line][column] = colour
        return matrix
    except IndexError:
        return matrix