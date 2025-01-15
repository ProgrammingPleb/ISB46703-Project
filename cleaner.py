import os
import shutil

for folder in os.listdir("dataset"):
    renameFolderParts = folder.replace(" ✅", "").strip().split(" ")
    
    newFolderParts = []
    for part in renameFolderParts:
        newFolderParts.append(part[0].upper() + part[1:])
    
    pos = 1
    for file in os.listdir(f"dataset/{folder}"):
        shutil.move(f"dataset/{folder}/{file}", f"dataset/{folder}/RenameTemp-{pos}.jpg")
        pos += 1
    pos = 1
    for file in os.listdir(f"dataset/{folder}"):
        shutil.move(f"dataset/{folder}/{file}", f"dataset/{folder}/{pos}.jpg")
        pos += 1
    shutil.move(f"dataset/{folder}", f"dataset/{" ".join(newFolderParts)}")
