# import os
# with open('mmm.txt', 'r') as f:
#     file = f.read()
#     lines = 0
#     for i in file:
#         if i != '\n':
#             lines += 1
#     print(lines)

file = open("mmm.txt", "r")
lines = 0
 
# Reading from file
readed = file.read()
onlist = readed.split("\n")
 
for i in onlist:
    if i:
        lines += 1
print(lines)

   