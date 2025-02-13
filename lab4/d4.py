from datetime import datetime

d1 = datetime(2025, 2, 1, 12, 0, 0)  
d2 = datetime(2025, 2, 13, 12, 0, 0)  

difference = (d2 - d1).total_seconds()
print("Difference in seconds:", difference)
