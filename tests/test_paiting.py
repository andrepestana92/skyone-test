import unittest
from manipulators.paiting import paint_pixel, paint_column, paint_line
from manipulators.initialization import init_image


class TestPaiting(unittest.TestCase):
    def test_paint_pixel(self):
        image = paint_pixel(init_image(2, 2), 1, 0, (100, 100, 100))
        pixels = image.load()
        self.assertTrue(pixels[0, 1] == (100, 100, 100))

    def test_paint_column(self):
        image = paint_column(init_image(3, 3), 1, 0, 2, (100, 100, 100))
        pixels = image.load()
        for j in range(3):
            self.assertTrue(pixels[j, 1] == (100, 100, 100))

    def test_paint_line(self):
        image = paint_line(init_image(3, 3), 1, 2, 2, (100, 100, 100))
        pixels = image.load()
        for i in range(1, 3):
            self.assertTrue(pixels[2, i] == (100, 100, 100))


if __name__ == '__main__':
    unittest.main()
