# with open('1.txt', 'r') as firstfile, open('2.txt', 'a') as secondfile:
#     for line in firstfile:
#         secondfile.write(line)

# with open('2.txt',"r") as file:
#     print(file.read())

import os

filePath = "Pandas/DataFrame/HandlingMissingData/loc"
n = 31 # Initial files number
addFolderLen = 31

def addFolders(n):
    for x in range(1,n):
        with open(f"{filePath}/exercise_{x}.py","a") as fileopen:
            fileopen.close()

if(os.path.isdir(filePath)):
    folderLen = n
    if(len(os.listdir(filePath)) == 0):
        addFolders(folderLen)
    else:
        folderLen = len(os.listdir(filePath)) + addFolderLen
        addFolders(folderLen)

else:
    os.mkdir(filePath)
    addFolders(n)



