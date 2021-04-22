data = [5,2,4,3,1,10,8]

def selection_sort(data):

    for i in range(0, len(data)):
        minIndex = i
        for j in range(i+1, len(data)):
            if data[j] < data[minIndex]:
                minIndex = j
        if i != minIndex:
            data[i], data[minIndex] = data[minIndex], data[i]
    return data

print(selection_sort(data))