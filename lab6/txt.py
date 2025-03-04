filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Hello, world! \nThis is a sample text file.\nPython is fun!\n")

print(f"File '{filename}' created in the current directory.")