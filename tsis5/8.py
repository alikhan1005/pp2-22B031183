import re

def split_at_uppercase(txt):
    return re.findall(r'[A-Z][^A-Z]*', txt)
# program to split a string at uppercase letters.

word = input("Enter a word: ")

print(split_at_uppercase(word))\
'''
ProgramToConvertSnakeCaseString_ToCamelCaseString
['Program', 'To', 'Convert', 'Snake', 'Case', 'String_', 'To', 'Camel', 'Case', 'String']
'''