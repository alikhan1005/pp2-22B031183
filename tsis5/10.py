import re

def camel_to_snake(txt):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt)
    return snake_str.lower()

# Python program to convert a given camel case string to snake case.
word = input("enter a word: ")

print(camel_to_snake(word))