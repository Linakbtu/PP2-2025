import re

text = input("Enter a CamelCase string: ")
pattern = r'([a-z])([A-Z])'

result = re.sub(pattern, r'\1_\2', text).lower()
print("Snake case:", result)
