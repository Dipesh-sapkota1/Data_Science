import re

text = input("Enter text: ")

no_punct = re.sub(r'[^\w\s]', '', text)
print(no_punct)