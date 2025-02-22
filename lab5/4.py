import re

text = input("Enter a string: ")
pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, text)
print("Matches:", matches)
