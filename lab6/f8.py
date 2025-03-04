import os

filename = "sample.txt"

if os.path.exists(filename) and os.access(filename, os.W_OK):
    os.remove(filename)
    print("File deleted")
else:
    print("File cannot be deleted (does not exist or no access)")
