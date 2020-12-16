data = [3,8,2,7,6,4,1,5]



def bubble_sort(data):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped=True
    return data

print(bubble_sort(data))