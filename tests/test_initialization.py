import unittest
from manipulators.initialization import init_image, clear_image


class TestInitializationMethods(unittest.TestCase):
    def test_init_image(self):
        image = init_image(1, 2)
        self.assertTrue(image.size[0] is 2)
        self.assertTrue(image.size[1] is 1)

    def test_init_image_with_zero_columns(self):
        image = init_image(1, 0)
        self.assertTrue(image.load() is None)

    def test_clear_image(self):
        image = init_image(1, 2)
        new_image = clear_image(image)
        self.assertTrue(new_image.size[0] == image.size[0])
        self.assertTrue(new_image.size[1] == image.size[1])
        pixels = new_image.load()
        for j in range(new_image.size[0]):
            for i in range(new_image.size[1]):
                self.assertTrue(pixels[j, i] == (0, 0, 0))


if __name__ == '__main__':
    unittest.main()
