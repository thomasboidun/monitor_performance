import unittest
from src.capture.capture import capture_scene

class TestCapture(unittest.TestCase):

    def test_capture_scene(self):
        result = capture_scene()
        self.assertTrue(isinstance(result, float))

if __name__ == '__main__':
    unittest.main()
