data = [10,15,22,27,30,36,38,42,48,50,65,68,72,74,80]



def binary_search(data, value, start , end):
    if start > end:
        return f"{value} not found in the list"

    middleIndex = (start+end)//2
    if value == data[middleIndex]:
        return middleIndex
    elif value > data[middleIndex]:
        return binary_search(data, value, middleIndex+1, end)
    else:
        return binary_search(data, value, 0, middleIndex-1)

print(binary_search(data, 150, 0, len(data)-1))