from PIL import Image


def init_image(lines, columns):
    return Image.new('RGB', (columns, lines))


def clear_image(image):
    return init_image(image.size[1], image.size[0])
