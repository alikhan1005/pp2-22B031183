import re


word = input("Enter a word: ")
pattern = r"^a.*b$"

# program that matches a string that has an 'a' followed by anything, ending in 'b'.

finding = re.match(pattern, word)

if finding:
    print("starts with a and ends with b")
else:
    print("does not")
