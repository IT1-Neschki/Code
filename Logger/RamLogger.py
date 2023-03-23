import psutil
import logging

logging.basicConfig(filename='memory.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

mem = psutil.virtual_memory()
ram_percent = mem.percent

if ram_percent >= 40:
    logging.warning(f"RAM usage is {ram_percent}%, which is over the warning threshold.")

logging.info(f"RAM usage: {ram_percent}%")