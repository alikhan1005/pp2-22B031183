import re

def snake_to_camel(txt):
    # return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), txt)
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))

# program to convert snake case string to camel case string.  
string = input("Enter a snake case string: ")

replace = snake_to_camel(string)

print(replace)
