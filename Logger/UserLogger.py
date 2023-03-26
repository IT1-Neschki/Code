import os

# Benutzerinformationen auslesen
output = os.popen('query user').read().strip().split('\n')

# Ergebnisse in eine Datei schreiben
with open('angemeldete_benutzer.txt', 'a') as file:  # Anstatt 'w' verwenden wir 'a', um die Datei fortzusetzen.
    for line in output:
        file.write(f'{line}\n')  # Formatieren Sie die Ausgabe, um sie untereinander zu schreiben.
