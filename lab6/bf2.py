text = input("Enter a string: ")
upper_count = sum(1 for c in text if c.isupper())
lower_count = sum(1 for c in text if c.islower())

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)