import psutil
import time
import datetime
import sys
import os

# Verzeichnis des aktuellen Skripts (DiskLogger.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Verzeichnis des Moduls sending_mail relativ zum Verzeichnis des aktuellen Skripts
sending_mail_dir = os.path.join(current_dir, '..', 'Dienste')

# Verzeichnis des Moduls sending_mail zum Suchpfad hinzufügen
sys.path.append(sending_mail_dir)

import sending_mail

# Festlegen der Grenzwerte
soft_limit = 70
hard_limit = 90

# Netzwerkname der Maschine
hostname = psutil.net_if_addrs()['WLAN'][0].address

# CPU-Frequenz abrufen und in MHz konvertieren
cpu_freq = psutil.cpu_freq().current / 1000

# CPU-Auslastung abrufen
cpu_usage = psutil.cpu_percent()

# Aktuelles Datum und Uhrzeit im ISO-Format abrufen
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

# Überprüfen und Erstellen der Logdatei
log_file = 'WarnungsLog.txt'
if not os.path.isfile(log_file):
    with open(log_file, 'w') as f:
        f.write('Logdatei erstellt am {}\n'.format(datetime.datetime.now()))

# Funktion zum Schreiben in die Logdatei
def write_log(message):
    with open(log_file, 'a') as logfile:
        logfile.write(message + '\n')  # Hinzufügen von '\n' am Ende der Nachricht

# Erstellen der Auslastungs-Logdatei
auslastungs_log = 'AuslastungsLog.txt'
if not os.path.isfile(auslastungs_log):
    with open(auslastungs_log, 'a') as f:
         f.write('Logdatei erstellt am {}\n'.format(datetime.datetime.now()))

# CPU-Frequenz und Auslastung in die Log-Datei schreiben
with open(auslastungs_log, "a") as logfile:
    logfile.write(f"{timestamp}, {hostname}, CPU-Frequenz: {cpu_freq:.2f}GHz & CPU-Auslastung: {cpu_usage:.2f}%\n")

# E-Mail-Versand bei Überschreitung des Hardlimits
if cpu_usage > hard_limit:
    message = '{} - {} - ERROR: CPU Auslastung bei {}%'.format(
        datetime.datetime.now(), hostname, cpu_usage)
    write_log(message)
    subject = 'CPU zu hoch bei {}%'.format(hostname)
    body = 'CPU Auslastung ist bei {}%.'.format(cpu_usage)
    sending_mail.send_email(subject, body)