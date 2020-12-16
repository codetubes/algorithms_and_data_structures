data = [3,8,2,7,6,4,1,5]



def merge(array1, array2):
    result = []
    i,j = 0,0

    while i< len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1

    while i < len(array1):
        result.append(array1[i])
        i+=1

    while j < len(array2):
        result.append(array2[j])
        j+=1

    return result

def devide(array):
    if len(array)<2:
        return array
    else:
        middle = len(array)//2
        left_array = devide(array[0:middle])
        right_array = devide(array[middle:])
        return merge(left_array,right_array)

def merge_sort(data):
    return devide(data)

print(merge_sort(data))