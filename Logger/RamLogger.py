import psutil
import datetime
import os
import sending_mail

# Netzwerkname der Maschine
hostname = psutil.net_if_addrs()['WLAN'][0].address

soft_limit = 1
hard_limit = 2

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

# Warnung bei Überschreitung des Softlimits
if used_percent > soft_limit:
    message = '{} - {} - WARNING: Ram usage at {}%'.format(
        datetime.datetime.now(), hostname, used_percent)
    write_log(message)

    # E-Mail-Versand bei Überschreitung des Hardlimits
if used_percent > hard_limit:
    message = '{} - {} - ERROR: Ram usage at {}%'.format(
        datetime.datetime.now(), hostname, used_percent)
    write_log(message)
    subject = 'Ram space exceeded on {}'.format(hostname)
    body = 'Ram usage is at {}%.'.format(used_percent)
    sending_mail.send_email(subject, body)