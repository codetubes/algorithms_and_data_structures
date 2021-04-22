data = [5,2,4,3,1,10,8]


def insertion_sort(data):
    for i in range(1, len(data)):

        j = i-1
        while data[j] > data[j+1] and j >=0:
            data[j], data[j+1]=data[j+1], data[j]
            j -=1
    return data


print(insertion_sort(data))