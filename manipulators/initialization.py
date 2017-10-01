from PIL import Image


def init_image(lines, columns):
    return Image.new('RGB', (columns, lines))


def clear_image(image):
    return Image.new('RGB', (image.size[0], image.size[1]))
