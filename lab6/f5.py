items = ["apple", "banana", "cherry"]
filename = "list.txt"

with open(filename, "w") as file:
    for item in items:
        file.write(item + "\n")

print("List written to file")
