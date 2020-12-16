#[2->4>10->5->12]

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Queue():


    def __init__(self):
        self.head = None
        self.tail = Node

    def add(self, x):
        if not isinstance(x, Node):
            x=Node(x)

        if self.head is None:
            self.head = x
        else:
            self.tail.next = x
        self.tail =x

    def remove(self):
        '''remove the first elemtn form the queue'''
        if self.head is None:
            return "List is empty"
        else:
            element = self.head
            self.head = self.head.next
            return element
    def peek(self):
        '''return the first element in the Queue'''
        if self.head is None:
            return "The list is empty"
        else:
            return self.head
    def is_empty(self):
        return self.head == None

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            current = self.head
            output = ""
            while current != None:
                output+= f"{current.data}->"
                current = current.next
            output = "["+output[:-2]+"]"
            return output

myQueue = Queue()
myQueue.add(10)
myQueue.add(5)
myQueue.add(6)
myQueue.add(4)
print(myQueue.remove())
print(myQueue)
