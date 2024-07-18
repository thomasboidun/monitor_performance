import unittest
from src.monitor.monitor import collect_system_metrics

class TestMonitorPerformance(unittest.TestCase):

    def test_collect_system_metrics(self):
        metrics = collect_system_metrics()
        self.assertIn("cpu_usage", metrics)
        self.assertIn("memory_total", metrics)
        self.assertIn("gpu_usage", metrics)

if __name__ == "__main__":
    unittest.main()
