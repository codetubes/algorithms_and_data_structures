data = [5,1,4,3,2,10,8]
data_best = [1,2,3,4,5,8,10]
data_worst = [10,8,5,4,3,2,1]

def bubble_sort(data):

    for i in range(0, len(data) -1):
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

print(bubble_sort(data_worst))