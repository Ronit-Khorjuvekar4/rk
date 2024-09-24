import os
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

origin = ROOT_DIR+'\Pandas\DataFrame\IndexingAndSelectingData\DataSet.py'
target = ROOT_DIR

print(origin)

shutil.move(origin,ROOT_DIR)
