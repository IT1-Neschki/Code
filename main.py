import time
import subprocess
import os

logger_dir = os.path.join(os.getcwd(), "Logger")

while True:
    subprocess.run(["python", os.path.join(logger_dir, "CPULogger.py")])
    subprocess.run(["python", os.path.join(logger_dir, "DiskLogger.py")])
    subprocess.run(["python", os.path.join(logger_dir, "RamLogger.py")])
    time.sleep(60)
