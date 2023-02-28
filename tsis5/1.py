import re

pattern = r'a+b*'
word = input("Enter a word: ")
find = re.match(pattern, word)

# program that matches a string that has an 'a' followed by zero or more 'b''s.
if find:
    print("matches")
else:
    print("does not")
