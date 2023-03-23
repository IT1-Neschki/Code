import psutil
import time
import datetime
import os
import sending_mail

# Festlegen der Grenzwerte
soft_limit = 2
hard_limit = 15

# Netzwerkname der Maschine
hostname = psutil.net_if_addrs()['Ethernet'][0].address

# Pfad zur Log-Datei im selben Ordner wie das Skript
log_file_path = "./CPU-Log.txt"

# Überprüfen, ob die Log-Datei vorhanden ist
if not os.path.exists(log_file_path):
    # Log-Datei erstellen, falls sie nicht vorhanden ist
    with open(log_file_path, "w") as log_file:
        log_file.write("Zeitstempel, CPU-Frequenz (MHz), CPU-Auslastung (%)\n")

# CPU-Frequenz abrufen und in MHz konvertieren
cpu_freq = psutil.cpu_freq().current / 1000

# CPU-Auslastung abrufen
cpu_usage = psutil.cpu_percent()

# Aktuelles Datum und Uhrzeit im ISO-Format abrufen
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

# CPU-Frequenz und Auslastung in die Log-Datei schreiben
with open(log_file_path, "a") as log_file:
    log_file.write(f"{timestamp}, {cpu_freq:.2f}, {cpu_usage:.2f}\n")
    
    # Warnung schreiben, falls CPU-Auslastung über Softlimit
    if cpu_usage > soft_limit:
        log_file.write(f"{timestamp}, CPU-Auslastung über 20%: {cpu_usage:.2f}\n")

# E-Mail-Versand bei Überschreitung des Hardlimits
if cpu_usage > hard_limit:
    message = '{} - {} - ERROR: CPU usage at {}%'.format(
        datetime.datetime.now(), hostname, cpu_usage)
    log_file.write(message)
    subject = 'CPU exceeded on {}'.format(hostname)
    body = 'CPU usage is at {}%.'.format(cpu_usage)
    sending_mail.send_email(subject, body)