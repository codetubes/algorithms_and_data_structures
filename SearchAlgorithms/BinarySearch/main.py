data = [10,15,22,27,30,36,38,42,48,50,65,68,72,74,80]


def binary_search(n, data, start, stop):

    if start > stop:
        return "Item Not found"
    else:
        middle = (start+stop)//2
        if n==data[middle]:
            return f"The {n}th element index is {middle}"
        elif n > data[middle]:
            return binary_search(n, data, middle+1, stop)
        else:
            return binary_search(n,data, start, middle-1)



print(binary_search(50,data, 0, len(data)-1))
