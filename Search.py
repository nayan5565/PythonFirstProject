pos = -1


def search(lst, sv):
    # p = 0
    for i in range(len(lst)):
        if lst[i] == sv:
            global pos
            pos = i
            return True
        # p += 1
    return False


def search_while(lst, sv):
    i = 0
    while i < len(lst):
        if lst[i] == sv:
            global pos
            pos = i
            return True
        i += 1
    return False


def search_binary(lst, sv):
    low = 0
    u = len(lst) - 1
    while low <= u:
        mid = (low + u) // 2
        if lst[mid] == sv:
            global pos
            pos = mid
            return True
        else:
            if lst[mid] < sv:
                low = mid + 1
            else:
                u = mid - 1
    return False


n = 7
list = [4, 7, 8, 12, 45, 99]
if search(list, n):
    print('found', pos)
else:
    print('not found')
