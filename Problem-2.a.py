import psutil
import time

# Predefined thresholds
CPU_Limit_Threshold = 80  # in percentage
MEMORY_Limit_Threshold = 75  # in percentage
DISK_Limit_Threshold = 85  # in percentage

def send_alert(message_text):
    # Send alert to console
    print(message_text)

def monitor_system(interval=1):
    while True:
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=interval)
        if cpu_percent > CPU_Limit_Threshold:
            alert_text = f"CPU usage exceeded it's limit threshold: {cpu_percent}%"
            send_alert(alert_text)

        # Memory usage
        memory_percent = psutil.virtual_memory().percent
        if memory_percent > MEMORY_Limit_Threshold:
            alert_text = f"Memory usage exceeded it's limit threshold: {memory_percent}%"
            send_alert(alert_text)

        # Disk usage
        disk_percent = psutil.disk_usage('/').percent
        if disk_percent > DISK_Limit_Threshold:
            alert_text = f"Disk usage exceeded it's limit threshold: {disk_percent}%"
            send_alert(alert_text)

        # Running processes
        num_processes = len(psutil.pids())
        if num_processes > 600:
            alert_text = f"Number of running processes exceeded it's limit threshold: {num_processes}"
            send_alert(alert_text)

        time.sleep(interval)

if __name__ == "__main__":
    monitor_system()
