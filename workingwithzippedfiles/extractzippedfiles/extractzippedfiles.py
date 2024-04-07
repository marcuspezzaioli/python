import os
from zipfile import ZipFile 

# Gets the current directory
path = os.getcwd()

# Gets the directories of the zipped files, and the directory we will zip too
zipped_path = path + "\zipped"
extracted_path = path + "\extracted"

for file in os.listdir(zipped_path): # Loops through everything in the Zipped directory
        with ZipFile(zipped_path + "/" + file, 'r') as zObject: 
                zObject.extractall(path=extracted_path)  # Extracts all files to Extracted directory