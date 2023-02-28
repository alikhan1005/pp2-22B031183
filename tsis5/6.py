import re

word = input("Enter a word: ")

# program to replace all occurrences of space, comma, or dot with a colon.

replace = re.sub(r'[ ,.]', ':', word)

print(replace)
