import math

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = math.prod(numbers)
print("Product of numbers:", result)