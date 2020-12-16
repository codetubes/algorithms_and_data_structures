data = [3,8,2,7,6,4,1,5]

def insertion_sort(data):

    marker = 1
    for i in range(marker, len(data)):
        while data[i-1] > data[i] and i > 0:
            data[i-1], data[i] = data[i], data[i-1]
            i-=1
    return data

print(insertion_sort(data))