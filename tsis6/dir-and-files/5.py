file = open('mmm.txt', 'w')
mylist = ['Alikhan', 'Alex', 'I am 18', 123, 123 ]
for i in mylist:
    file.write(str(i) + '\n')