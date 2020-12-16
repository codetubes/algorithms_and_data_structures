data = [5,2,7,4,1,3,6]


def insertion_sort(data):

    for i in range(1, len(data)):

        while data[i-1] > data[i] and i > 0:

            data[i], data[i-1] = data[i-1], data[i]
            i -=1
    print(data)

insertion_sort(data)

