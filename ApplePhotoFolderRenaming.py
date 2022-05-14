import re
import os
from datetime import date, datetime
import locale
import unicodedata

def renameApplePhotoFolder(dir, local='en'):
    locale.setlocale(locale.LC_TIME, local)

    for entry in os.scandir(dir):
        if os.path.isdir(entry):
            # Normalize Unicode. For ex. 'e' + '´' become 'é'
            folderName = unicodedata.normalize('NFC',entry.name) 
            # Handles rereading of changed folders
            matched = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}[,]?', folderName)
            if bool(matched):
                continue

            tokens = folderName.split(",")
            dateStr = tokens[-1]
            loc = ','.join(tokens[:-1])

            dateStr = dateStr.strip()
            date = datetime.strptime(dateStr, "%d %B %Y").date()

            folderName = date.isoformat()
            if loc != "":
                folderName += ", " + loc

            os.rename(entry.path, os.path.join(dir, folderName))

            print(f"{entry.name:<60} ->  {folderName}")



if __name__ == '__main__':
    srcDir = r'/Volumes/TOSHIBA EXT/backup-photos'
    renameApplePhotoFolder(srcDir, 'fr_FR')
