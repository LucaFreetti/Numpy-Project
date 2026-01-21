import os
import shutil
import csv
import argparse

# Traduttore parser
parser = argparse.ArgumentParser(description='Sposta il file indicato nella sua sottocartella ed aggiorna il recap')

#Argomento filename, corrispondente al file da inserire nel cli
parser.add_argument('filename', help='Inserisci il nome del file(incluso la sua estenzione)')

#Assegnazione dell'argomento
args = parser.parse_args()
filename = args.filename

#Percorso in cui é presente il file addfile.py
base_path = os.path.dirname(os.path.abspath(__file__))
files_path = base_path  

# Percorso del documento selezionato
filename_path = os.path.join(files_path, filename)

# Messaggi di errore
if not os.path.exists(filename_path):
    print(f"Errore: il file {filename} indicato non esiste all'interno della cartella")
    exit(1)
if not os.path.isfile(filename_path):
    print(f"Errore: {filename} non è un file")
    exit(1)

#Liste necessarie all'associazione del file nella rispettiva cartella, qualora si voglia inserire un file con estensione differente dai seguenti, inserire manualmente l'estensione nelle rispettive liste per non incappare in errore.
immagini = ['.png', '.jpeg', '.jpg']
audio = ['.mp3']
documenti = ['.txt', '.odt']

# Dimensione file
size = os.path.getsize(filename_path)

# Estensione del file
estensione = os.path.splitext(filename)[1].lower()

# Assegnazione del file nella rispettiva cartella
if estensione in immagini:
    tipo = 'immagine'
    folder_dest = 'immagini'
elif estensione in audio:
    tipo = 'audio'
    folder_dest = 'audio'
elif estensione in documenti:
    tipo = 'documento'
    folder_dest = 'documenti'
else:
    print(f'Errore: la estensione {estensione} non è supportata')
    exit(1)

# Percorso della cartella di destinazione finale
folder_dest_path = os.path.join(files_path, folder_dest)

# Se non esiste creala
if not os.path.exists(folder_dest_path):
    os.mkdir(folder_dest_path)

# Percorso finale del file
dest_filename_path = os.path.join(folder_dest_path, filename)

# Muovere il file
shutil.move(filename_path, dest_filename_path)
print(f"Il file {filename} è un {tipo} con un peso di {size} bytes")

# Creazione file di recap csv
csv_path = os.path.join(files_path, 'recap.csv')
recap_exist = os.path.exists(csv_path)

with open(csv_path, mode='a', newline='', encoding='utf-8') as recap_file:
    writer = csv.writer(recap_file)
    if not recap_exist:
        writer.writerow(['nome', 'tipo', 'dimensione'])
    writer.writerow([filename, tipo, size])

print(f"File spostato con successo e recap.csv aggiornato!")