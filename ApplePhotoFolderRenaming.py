import re
import os
from datetime import date, datetime
import locale

def renameApplePhotoFolder(dir, local='en'):
    locale.setlocale(locale.LC_TIME, local)

    for entry in os.scandir(dir):
        if os.path.isdir(entry):

            # Handles rereading of changed folders
            matched = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}[,]?', entry.name)
            if bool(matched):
                continue

            tokens = entry.name.split(",")
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
    
    renameApplePhotoFolder(r'E:\Export\Photos', 'fr_FR')
