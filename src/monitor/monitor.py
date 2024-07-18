import time
import psutil
import GPUtil

def collect_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=None)  # Ne pas attendre 1 seconde pour obtenir le pourcentage
    memory_info = psutil.virtual_memory()
    gpu_info = GPUtil.getGPUs()

    metrics = {
        "cpu_usage": cpu_usage,
        "memory_total": memory_info.total / (1024 ** 3),  # Convertir en GB
        "memory_available": memory_info.available / (1024 ** 3),  # Convertir en GB
        "memory_used": memory_info.used / (1024 ** 3),  # Convertir en GB
        "memory_percentage": memory_info.percent,
        "gpu_usage": []
    }

    for gpu in gpu_info:
        metrics["gpu_usage"].append({
            "id": gpu.id,
            "name": gpu.name,
            "load": gpu.load,
            "memory_total": gpu.memoryTotal / 1024,  # Convertir en GB
            "memory_used": gpu.memoryUsed / 1024,  # Convertir en GB
            "memory_free": gpu.memoryFree / 1024,  # Convertir en GB
            "temperature": gpu.temperature
        })

    return metrics

def monitor_performance(performance_data, stop_event, sample_rate):
    interval = 1 / sample_rate  # Intervalle de collecte des métriques (en secondes)
    start_time = time.time()

    while not stop_event.is_set():
        metrics = collect_system_metrics()
        current_time = time.time()
        performance_data.append({
            "time": current_time - start_time,  # Temps relatif à zéro
            "metrics": metrics
        })
        time.sleep(interval)
