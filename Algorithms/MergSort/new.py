data = [8,5,2,7,6,4,1,3]

def sort(array1, array2):
    result = []
    i = 0
    j = 0

    while( i< len(array1) and j< len(array2)):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1

    while i<len(array1):
        result.append(array1[i])
        i+=1

    while j < len(array2):
        result.append(array2[j])
        j+=1

    return result

def merge_sort(data):
    if len(data)<2:
        return data
    else:
        middle = len(data)//2
        left_merge = merge_sort(data[0:middle])
        right_merge = merge_sort(data[middle:])
        return sort(left_merge, right_merge)

print(merge_sort(data))
