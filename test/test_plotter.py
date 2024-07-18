import unittest
from src.plotter.plotter import plot_performance_data

class TestPlotter(unittest.TestCase):

    def test_plot_data(self):
        json_file = "test/sample/performance_data.json"
        output_dir = "test/sample"
        result = plot_performance_data(json_file, output_dir)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
