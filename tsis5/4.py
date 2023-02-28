 #  Enter a sentence: Alcidsc sjfb adcjaA vfjfv Acfsrvj
 # ['Alcidsc', 'Acfsrvj'] 

import re   
sentence = input("Enter a sentence: ")

pattern = r"[A-Z][a-z]+"
# program to find the sequences of one upper case letter followed by lower case letters.

finding = re.findall(pattern, sentence)

print(finding)

