data = [3,8,2,7,6,4,1,5]


def selection_sort(data):

    marker = 0
    while marker < len(data):
        lowerIndex = marker
        for i in range(marker, len(data)-1):
            if data[i] < data[lowerIndex]:
                lowerIndex = i
        data[lowerIndex], data[marker] = data[marker], data[lowerIndex]
        marker+=1
    return data

print(selection_sort(data))