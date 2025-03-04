import time
import math

number = int(input("Enter a number: "))
delay = int(input("Enter delay in milliseconds: "))

time.sleep(delay / 1000) 
print("Square root of the number:", math.sqrt(number))