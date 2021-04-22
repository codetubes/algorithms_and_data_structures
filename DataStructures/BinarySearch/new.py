data = [10,15,22,27,30,36,38,42,48,50,65,68,72,74,80]



def binary_search(number, data, start, stop):
    #if start > stop:
    #    return f"{number} not found in the list"

    middle = (start+stop)//2

    if number == data[middle]:
        return f"Number {number} found at index {middle}"
    elif number > data[middle]:
        return binary_search(number, data, middle+1, stop)
    else:
        return binary_search(number, data, start, middle-1)




def search(number, data):
    return binary_search(number, data, 0, len(data)-1)

print(search(150, data))
