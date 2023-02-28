import re

def insert_spaces(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

# (\w)([A-Z])ищем места, где после любого слова идет заглавная буква
# r"\1 \2"  - это ссылки на первую и вторую группы в шаблоне 
#  program to insert spaces between words starting with capital letters.

words = input()
insert = insert_spaces(words)

print(insert)