data = [10,15,22,35,42,50,61,72,84]
#50

def binary_search(number, data, start, end):
    if start > end:
        return f"{number} not found in the list"


    middle = (start+end)//2
    if number == data[middle]:
        return f"Number {number} found at index {middle}"
    elif number > data[middle]:
        return binary_search(number, data,middle+1, end)
    else:
        return binary_search(number, data,start, middle-1)


print(binary_search(120,data, 0, len(data)-1))