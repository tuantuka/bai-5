def sequential_Search(alist, items):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == items:
            found = True
        else:
            pos += 1
    return found, pos

alist = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
items = 31
print(sequential_Search(alist, items))