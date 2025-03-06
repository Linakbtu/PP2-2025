for letter in range(65, 91):  
    filename = chr(letter) + ".txt"
    with open(filename, "w") as file:
        file.write(f"This is {filename}\n")

print("26 files created")
