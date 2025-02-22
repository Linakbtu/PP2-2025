import re

text = input("Enter a string: ")
pattern = r'(?=[A-Z])'

result = re.split(pattern, text)
print("Split result:", result)
