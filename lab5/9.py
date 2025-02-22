import re

text = input("Enter a string: ")
pattern = r'([a-z])([A-Z])'

result = re.sub(pattern, r'\1 \2', text)
print("Modified string:", result)
