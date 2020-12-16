data = [3,5,2,7,6,8,1,4]


def sort(data1, data2):

    i, j = 0,0
    sorted = []
    while i < len(data1) and j < len(data2):
        if data1[i] > data2[j]:
            sorted.append(data2[j])
            j+=1
        else:
            sorted.append(data1[i])
            i+=1


    while i < len(data1):
        sorted.append(data1[i])
        i+=1

    while j < len(data2):
        sorted.append(data2[j])
        j+=1

    return sorted





def devide(data):
    if len(data) < 2:
        return data

    middle = len(data)//2
    left = devide(data[:middle])
    right = devide(data[middle:])
    return sort(left,right)

def merge_sort(data):
    return devide(data)

data1 = [1,4,6,8]
data2 = [2,3,5,7]
print(merge_sort(data))