def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Unique elements:", unique_elements(numbers))
