import os

class Folder:
    def __init__(self):
        self.path = os.getcwd()
        name = ""
        self.getListFiles()        
                
    def getPath(self):
        return self.path
    
    def getListFiles(self):
        self.listFiles = {""}
        self.listFiles.remove("")
        for entry in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, entry)):
                self.listFiles.add(entry)
        