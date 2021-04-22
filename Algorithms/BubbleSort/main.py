data = [5,1,4,3,2,10,8]
data_best = [1,2,3,4,5,8,10]
data_worst = [10,8,5,4,3,2,1]

def bubble_sort(data):
    steps = 0
    swapped = True
    while swapped:
        steps+=1
        swapped = False
        for i in range(len(data)-1):
            steps+=1
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
                print(data)
    print(data)
    print(steps)


bubble_sort(data)



