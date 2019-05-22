def binary_search(list, value):
    first = 0
    last = len(list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == value:
            found = True
        else:
            if value < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(list, 3))
print(binary_search(list, 13))