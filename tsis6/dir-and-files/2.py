# R_OK, W_OK, and X_OK to test permissions.  os.access(path, mode)
import os

path = '/Users/alikhankudaibergen/documents/pp2'

if os.path.exists(path):
    print("This file exists")
if os.access(path, os.R_OK):
    print("This file is readable")
if os.access(path, os.W_OK):
    print("This file is writeable")
if os.access(path, os.X_OK):
    print("This file is executable")