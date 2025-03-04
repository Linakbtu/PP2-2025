def all_true(t):
    return all(t)

values = tuple(map(bool, map(int, input("Enter numbers separated by spaces (0 = False, others = True): ").split())))
print("All elements are true:", all_true(values))