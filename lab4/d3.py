from datetime import datetime

now = datetime.now().replace(microsecond=0)
print("Time without microseconds:", now)
