import psutil
import datetime
import os
import sys
import os

# Verzeichnis des aktuellen Skripts (DiskLogger.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Verzeichnis des Moduls sending_mail relativ zum Verzeichnis des aktuellen Skripts
sending_mail_dir = os.path.join(current_dir, '..', 'Dienste')

# Verzeichnis des Moduls sending_mail zum Suchpfad hinzufügen
sys.path.append(sending_mail_dir)

import sending_mail

# Netzwerkname der Maschine
hostname = psutil.net_if_addrs()['WLAN'][0].address

soft_limit = 1
hard_limit = 2

# Netzwerkname der Maschine
hostname = psutil.net_if_addrs()['WLAN'][0].address

# Überprüfen und Erstellen der Logdatei
log_file = 'WarnungsLog.txt'
if not os.path.isfile(log_file):
    with open(log_file, 'w') as f:
        f.write('Logdatei erstellt am {}\n'.format(datetime.datetime.now()))

# Funktion zum Schreiben in die Logdatei
def write_log(message):
    with open(log_file, 'a') as logfile:
        logfile.write(message + '\n')  # Hinzufügen von '\n' am Ende der Nachricht

#Überprüfung der Ram Auslastung
mem = psutil.virtual_memory()
used_percent = mem.percent

# Erstellen der Auslastungs-Logdatei
auslastungs_log = 'AuslastungsLog.txt'
with open(auslastungs_log, 'a') as f:
    f.write('Logdatei erstellt am {}\n'.format(datetime.datetime.now()))

# Schreiben der aktuellen Ram-Auslastung in die Auslastungs-Logdatei
with open(auslastungs_log, 'a') as logfile:
    logfile.write('{} - {} - Ramauslastung bei {}%\n'.format(
        datetime.datetime.now(), hostname, used_percent))

# Warnung bei Überschreitung des Softlimits
if used_percent > soft_limit:
    message = '{} - {} - WARNING: Ramauslastung bei {}%'.format(
        datetime.datetime.now(), hostname, used_percent)
    write_log(message)

    # E-Mail-Versand bei Überschreitung des Hardlimits
if used_percent > hard_limit:
    message = '{} - {} - ERROR: Ramauslastung bei {}%'.format(
        datetime.datetime.now(), hostname, used_percent)
    write_log(message)
    subject = 'Ramauslastung zu hoch bei {}'.format(hostname)
    body = 'Ramauslastung bei {}%.'.format(used_percent)
    sending_mail.send_email(subject, body)