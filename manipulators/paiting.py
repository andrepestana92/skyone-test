def paint_pixel(image, line, column, colour):
    if line < image.size[1] and column < image.size[0]:
        pixels = image.load()
        pixels[column, line] = colour
    return image
