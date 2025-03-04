filename = "sample.txt"

with open(filename, "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))
