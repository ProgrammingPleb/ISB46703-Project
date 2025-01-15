import os

allFolders = os.listdir("base-dataset")
allFolders.sort()

data = {}

for folder in allFolders:
    data[folder] = len(os.listdir(f"base-dataset/{folder}"))
    newData = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

print("Top Species")

pos = 1
total = 0
for key in list(newData.keys())[0:5]:
    print(f"{pos}. {key} - {newData[key]}")
    pos += 1
    total += newData[key]
print(f"Top 5 Total: {total}")

print(f"\nTotal: {len(allFolders)} species")
