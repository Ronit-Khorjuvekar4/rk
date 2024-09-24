import os
import shutil

origin = "Pandas\DataFrame\IndexingAndSelectingData"
target = "Pandas/DataFrame/IndexingAndSelectingData"

files = os.listdir(origin)
osPath = os.path.isfile(origin)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# shutil.copytree(origin, target)

length = len(os.listdir(origin))

for i in range(length):
    os.remove(f'{ROOT_DIR}\{origin}\{files[i]}')
    print(f'{ROOT_DIR}\{origin}\{files[i]}')
else:
    os.rmdir(f'{ROOT_DIR}\{origin}')