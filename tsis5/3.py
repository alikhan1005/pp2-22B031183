import re

sentence = input("Enter a sentence: ")
pattern = r"[a-z]+_[a-z]+"
# program to find sequences of lowercase letters joined with a underscore.

finding = re.findall(pattern, sentence)

for i in finding:
    print(i)
