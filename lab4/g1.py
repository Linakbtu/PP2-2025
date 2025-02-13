def squares_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input("Enter a number N: "))  
for num in squares_generator(N):
    print(num)
