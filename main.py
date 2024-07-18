from src.capture.capture import run_capture_with_monitoring
from src.plotter.plotter import plot_performance_data

if __name__ == "__main__":
    sample_rate = 3
    output_dir = "output"
    json_file = run_capture_with_monitoring(output_dir, sample_rate)
    plot_performance_data(json_file, output_dir)
