import psutil
import logging
import datetime
import sending_mail

# Netzwerkname der Maschine
hostname = psutil.net_if_addrs()['Ethernet'][0].address

hard_limit = 40

logging.basicConfig(filename='memory.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

mem = psutil.virtual_memory()
used_percent = mem.percent

if used_percent >= hard_limit:
    logging.warning(f"RAM usage is {used_percent}%, which is over the warning threshold.")

logging.info(f"RAM usage: {used_percent}%")

    # E-Mail-Versand bei Überschreitung des Hardlimits
if used_percent > hard_limit:
    message = '{} - {} - ERROR: Disk usage at {}%'.format(
        datetime.datetime.now(), hostname, used_percent)
    write_log(message)
    subject = 'Hard disk space exceeded on {}'.format(hostname)
    body = 'Disk usage is at {}%.'.format(used_percent)
    sending_mail.send_email(subject, body)