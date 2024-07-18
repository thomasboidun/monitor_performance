import json
import os
import matplotlib.pyplot as plt

def plot_performance_data(json_file, output_dir):
    with open(json_file, "r") as f:
        performance_data = json.load(f)

    times = [snapshot["time"] for snapshot in performance_data["performance"]]
    cpu_usages = [snapshot["metrics"]["cpu_usage"] for snapshot in performance_data["performance"]]
    memory_usages = [snapshot["metrics"]["memory_used"] for snapshot in performance_data["performance"]]

    gpu_memory_usages = [
        sum(gpu["memory_used"] for gpu in snapshot["metrics"]["gpu_usage"])
        for snapshot in performance_data["performance"]
    ]

    total_gpu_memory = sum(gpu["memory_total"] for gpu in performance_data["performance"][0]["metrics"]["gpu_usage"])

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(times, cpu_usages, label="CPU Usage (%)")
    plt.xlabel("Time (s)")
    plt.ylabel("CPU Usage (%)")
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(times, memory_usages, label="Memory Usage (GB)")
    plt.xlabel("Time (s)")
    plt.ylabel("Memory Usage (GB)")
    plt.ylim(0, max(memory_usages) * 1.1)
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(times, gpu_memory_usages, label="GPU Memory Usage (GB)")
    plt.xlabel("Time (s)")
    plt.ylabel("GPU Memory Usage (GB)")
    plt.ylim(0, total_gpu_memory * 1.1)
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_image = os.path.join(output_dir, "performance_plot.png")
    plt.savefig(output_image)
    plt.close()
