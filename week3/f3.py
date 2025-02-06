def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return None

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
if result:
    print(f"Chickens: {result[0]}, Rabbits: {result[1]}")
else:
    print("No solution found")
