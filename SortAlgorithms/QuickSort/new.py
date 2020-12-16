data = [3,5,2,7,6,8,1,4]


def qs_easy(data):
    if len(data)<2:
        return data

    pivot = data.pop()
    smaller, larger = [],[]
    for item in data:
        if item < pivot:
            smaller.append(item)
        else:
            larger.append(item)
    return qs_easy(smaller)+[pivot]+qs_easy(larger)

def sort(data, l, r):
    pivotIndex = get_pivot(data, l,r)#r
    pivotValue = data[pivotIndex]#data[r]

    data[l], data[pivotIndex] = data[pivotIndex], data[l]
    border = l
    for i in range(l, r+1):
        if data[i] < pivotValue:
            border+=1
            data[border], data[i] = data[i], data[border]
    data[l], data[border] = data[border], data[l]
    return border


def qs_inplace(data, l, r):
    if l<r:
        border = sort(data, l, r)
        qs_inplace(data, l,border-1)
        qs_inplace(data, border+1, r)








def get_pivot(data, l,r):
    middleIndex = (l+r)//2

    if (data[l] >= data[r] and data[l]<= data[middleIndex]) or \
            (data[l]<= data[r] and data[l] >= data[middleIndex]):
        pivotIndex = l
    elif (data[r] >= data[l] and data[r]<= data[middleIndex]) or \
            (data[r]<= data[l] and data[r] >= data[middleIndex]):
        pivotIndex = r
    elif (data[middleIndex] >= data[l] and data[middleIndex]<= data[r]) or \
            (data[middleIndex]<= data[l] and data[middleIndex] >= data[r]):
        pivotIndex = middleIndex
    return pivotIndex


def quick_sort(data):
    #return qs_easy(data)
    qs_inplace(data, 0, len(data)-1)

quick_sort(data)
print(data)