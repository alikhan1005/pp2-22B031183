file = open('mmm.txt', 'r')
copy = open('www.txt', 'w')
# copy.write(str(file))
for i in file:
    copy.write(str(i))

copy.close()
copy = open('www.txt', 'r')
print(copy.read())