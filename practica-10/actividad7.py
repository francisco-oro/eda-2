# Recorrer un directorio
import os
rootDir = 'C:\\Users\\ASUS'

for dirName, subdirList, fileList in os.walk(rootDir):
    print(f'Directorio encontrado: {dirName}')
    for fname in fileList:
        print(f'\t {fname}')