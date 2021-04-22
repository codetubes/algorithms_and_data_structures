data = [8,5,2,7,6,4,1,3]
data1 = [2,5,7,8]
data2 = [1,3,4,6]


def sort(array1, array2):
    print("Array1: ", array1)
    print("Array2: ", array2)
    print("==================")
    result = []
    i,j = 0,0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1

    while j < len(array2):
        result.append(array2[j])
        j+=1

    while i < len(array1):
        result.append(array1[i])
        i+=1


    return result

def devide(data):

    if len(data)<2:
        return data
    else:
        middle = len(data)//2
        array1 = devide(data[0:middle])
        array2 = devide(data[middle:])
        return sort(array1, array2)


print(devide(data))