data = [5,2,7,4,1,3,6]


def selection_sort(data):
    marker = 0
    while marker<len(data):
        min_index = marker
        for i in range(marker, len(data)):
            if data[marker] > data[i]:
                if data[i] < data[min_index]:
                    min_index = i
        data[marker], data[min_index] = data[min_index], data[marker]
        marker+=1

    print(data)



selection_sort(data)

