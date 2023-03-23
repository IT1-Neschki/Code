import psutil
import time
import os

# Pfad zur Log-Datei im selben Ordner wie das Skript
log_file_path = "./Log.txt"

# Überprüfen, ob die Log-Datei vorhanden ist
if not os.path.exists(log_file_path):
    # Log-Datei erstellen, falls sie nicht vorhanden ist
    with open(log_file_path, "w") as log_file:
        log_file.write("CPU-Frequenz (MHz), CPU-Auslastung (%)\n")

# CPU-Frequenz abrufen und in MHz konvertieren
cpu_freq = psutil.cpu_freq().current / 1000

# CPU-Auslastung abrufen
cpu_usage = psutil.cpu_percent()

# Aktuelles Datum und Uhrzeit im ISO-Format abrufen
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

# CPU-Frequenz und Auslastung in die Log-Datei schreiben
with open(log_file_path, "a") as log_file:
    log_file.write(f"{timestamp}, {cpu_freq:.2f}, {cpu_usage:.2f}\n")
