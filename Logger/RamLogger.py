import psutil
import logging

logging.basicConfig(filename='memory.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

mem = psutil.virtual_memory()
ram_percent = mem.percent

logging.info(f"RAM usage: {ram_percent}%")
