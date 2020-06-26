#Programa para leitura e organização de fotos
from src.Folder import Folder
import os


myFolder = Folder()

for n in myFolder.listFiles:
    print(n)