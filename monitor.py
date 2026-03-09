import psutil

# CPU usage
cpu = psutil.cpu_percent(interval=1)

# Memory usage
memory = psutil.virtual_memory()

# Disk usage
disk = psutil.disk_usage('/')

print("CPU Usage:", cpu, "%")
print("Memory Usage:", memory.percent, "%")
print("Disk Usage:", disk.percent, "%")
