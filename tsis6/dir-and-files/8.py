#  os.remove(fname + ".txt")    
import os

path = '/Users/alikhankudaibergen/documents/pp2/tsis6/delete.txt'
if os.path.exists(path):
    print("a given path exists")
    os.remove(path)  
else:
    print("does not exists")