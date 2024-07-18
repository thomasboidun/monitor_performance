import time
import random
import json
import threading
import os
from src.monitor.monitor import monitor_performance

def capture_scene():
    duration = random.uniform(5, 30)
    time.sleep(duration)
    return duration

def run_capture_with_monitoring(output_dir, sample_rate=3):
    performance_data = []
    stop_event = threading.Event()

    performance_info = {
        "name": "snapshot_image.png",
        "scene": {
            "model": {
                "id": "model_id_123",
                "file": "model_file.obj",
                "size": "15MB",
                "config": "model_config_string"
            },
            "decor": {
                "id": "decor_id_456",
                "file": "decor_file.obj",
                "size": "10MB"
            },
            "animation": {
                "id": "animation_id_789",
                "type": "camera"
            },
            "hotspots": []
        },
        "configs": {
            "resolution": {
                "width": 1920,
                "height": 1080
            },
            "format": {
                "extension": "png",
                "compression": "lossless"
            }
        },
        "duration": 0,
        "performance": performance_data
    }

    monitor_thread = threading.Thread(target=monitor_performance, args=(performance_data, stop_event, sample_rate))

    print("Starting snapshot capture and performance monitoring...")

    monitor_thread.start()

    capture_duration = capture_scene()

    stop_event.set()
    monitor_thread.join()

    print("Snapshot capture and performance monitoring complete.")

    performance_info["duration"] = capture_duration

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "performance_data.json")
    with open(output_file, "w") as f:
        json.dump(performance_info, f, indent=4)
    
    return output_file
