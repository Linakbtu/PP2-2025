import os

path = "sample.txt"  

print("Directories:", [d for d in os.listdir(path) if os.path.isdir(d)])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(f)])
print("All:", os.listdir(path))
