import os

filePath = "Pandas/DataManipulation/AddingColumns"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

len = len(os.listdir(filePath))

for x in range(0,len):
    dataset = open(f'{ROOT_DIR}/DataSet.py', "r")
    fpath = os.listdir(filePath)[x] 
    if(fpath.find('exe') == 0 ):
        if(os.path.getsize(f'{filePath}/{fpath}') == 0):
            file2 = open(f'{filePath}/{fpath}', "a")
            file2.write(dataset.read())
            file2.close()
            dataset.close()