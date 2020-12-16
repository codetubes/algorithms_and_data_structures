data = [3,8,2,7,6,4,1,5]
def qs_easy(data):
    if len(data)<2:
        return data

    smaller, larger = [],[]
    pivot = data.pop()

    for item in data:
        if item < pivot:
            smaller.append(item)
        else:
            larger.append(item)
    return qs_easy(smaller) + [pivot] + qs_easy(larger)

def partition(data, l, r):
    pivotIndex = r
    pivotValue = data[r]
    border = l
    data[l], data[pivotIndex] = data[pivotIndex], data[l]
    for i in range(l,r+1):
        if data[i] < pivotValue:
            border+=1
            data[border], data[i] = data[i], data[border]
    data[border], data[l] = data[l], data[border]
    return border



def qs_inplace(data, l,r):
    if l<r:
        border = partition(data, l, r)
        qs_inplace(data,l, border-1)
        qs_inplace(data, border+1, r)
def quick_sort(data):
    qs_inplace(data, 0, len(data)-1)

quick_sort(data)
print(data)