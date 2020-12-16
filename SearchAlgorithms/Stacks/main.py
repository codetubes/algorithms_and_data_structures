

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Stack():

    def __init__(self):
        self.head = None

    def push(self,x):
        '''Add value to the stack'''
        if not isinstance(x, Node):
            x = Node(x)

        if self.head is None:
            self.head = x
        else:
            x.next = self.head
            self.head = x

    def pop(self):
        '''Remove the first element from the stack'''
        if self.head is None:
            return None
        else:
            element = self.head
            self.head = self.head.next
            return element

    def is_empty(self):
        '''check to see if the stack is empty'''
        return self.head == None

    def peek(self):
        """return the first element value in stack"""
        return self.head.data


    def __str__(self):
        if self.head is None:
            return "[]"
        else:
            current = self.head
            output = ""
            while current != None:
                output+= f"{current.data} \n-\n"
                current = current.next
            output = output[:-2]
            return output



myStack = Stack()
myStack.push(5)
myStack.push(2)
myStack.push(3)
myStack.push(11)
myStack.push(8)
print("popped element ->",myStack.pop().data)
print(myStack)