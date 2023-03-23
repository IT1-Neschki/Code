import time
import subprocess
import os

logger_dir = os.path.join(os.getcwd(), "Logger")
start_time = time.time()
max_runtime = 300  # seconds
loop_count = 0

while (time.time() - start_time) < max_runtime:
    subprocess.run(["python", os.path.join(logger_dir, "CPULogger.py")])
    subprocess.run(["python", os.path.join(logger_dir, "DiskLogger.py")])
    subprocess.run(["python", os.path.join(logger_dir, "RamLogger.py")])
    time.sleep(60)
    loop_count += 1

print(f"Script ran for {loop_count} loops and {time.time() - start_time} seconds.")