import re


pattern = r"a{1}b{2,3}"
word = input()
find = re.match(pattern, word)

# program that matches a string that has an 'a' followed by two to three 'b'.

if find:
    print("matches")
else:
    print("does not")