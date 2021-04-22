data = [3,5,2,7,6,8,1,4]

def partition(data, low, high):
    pivotIndex = high
    pivotValue = data[pivotIndex]

    data[low], data[pivotIndex] = data[pivotIndex], data[low]
    border = low
    for i in range(low, high+1):
        if data[i] < pivotValue:
            border+=1
            data[i], data[border] = data[border], data[i]

    data[border], data[low] = data[low], data[border]
    return border

def quick_sort2(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quick_sort2(data, low, p-1)
        quick_sort2(data, p+1, high)

def quick_sort(data):
    return quick_sort2(data, 0, len(data)-1)

quick_sort(data)
print(data)