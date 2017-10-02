import unittest
from pathlib import Path
from manipulators.paiting import paint_rectangle
from manipulators.initialization import init_image
from manipulators.saving_image import save_image

class TestSavingImage(unittest.TestCase):
    def test_save_image(self):
        image = paint_rectangle(init_image(4, 4), 0, 1, 0, 1, (100, 100, 100))
        name = 'TestFile'
        save_image(image, name)
        file = Path('TestFile.bmp')
        self.assertTrue(file.exists())
        file.unlink()

if __name__ == '__main__':
    unittest.main()