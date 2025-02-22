import re

text = input("Enter a string: ")
pattern = r'[ ,.]'
replacement = ':'

result = re.sub(pattern, replacement, text)
print("Modified string:", result)
