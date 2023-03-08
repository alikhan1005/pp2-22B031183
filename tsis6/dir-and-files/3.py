import os
path = '/Users/alikhankudaibergen/documents/pp2/tsis4/generators'
if os.path.exists(path):
    name = os.path.split(path)
    print(name)
    print(name[0])
    print(name[1])
    # for i in name:
    #     print(i)