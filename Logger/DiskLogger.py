import psutil
import datetime
import os
import sending_mail

# Festlegen der Grenzwerte
soft_limit = 2
hard_limit = 15

# Netzwerkname der Maschine
hostname = psutil.net_if_addrs()['Ethernet'][0].address

# Überprüfen und Erstellen der Logdatei
log_file = 'log.txt'
if not os.path.isfile(log_file):
    with open(log_file, 'w') as f:
        f.write('Logdatei erstellt am {}\n'.format(datetime.datetime.now()))

# Funktion zum Schreiben in die Logdatei
def write_log(message):
    with open(log_file, 'a') as logfile:
        logfile.write(message + '\n')  # Hinzufügen von '\n' am Ende der Nachricht

# Überprüfung des Festplattenspeichers
disk_usage = psutil.disk_usage('/')
used_percent = disk_usage.percent

# Warnung bei Überschreitung des Softlimits
if used_percent > soft_limit:
    message = '{} - {} - WARNING: Disk usage at {}%'.format(
        datetime.datetime.now(), hostname, used_percent)
    write_log(message)

# E-Mail-Versand bei Überschreitung des Hardlimits
if used_percent > hard_limit:
    message = '{} - {} - ERROR: Disk usage at {}%'.format(
        datetime.datetime.now(), hostname, used_percent)
    write_log(message)
    subject = 'Hard disk space exceeded on {}'.format(hostname)
    body = 'Disk usage is at {}%.'.format(used_percent)
    sending_mail.send_email(subject, body)
