

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackDS:

    def __init__(self):
        self.head = None

    def insert(self, element):
        if not isinstance(element, Node):
            element = Node(element)

        if self.head is None:
            self.head = element
        else:
            element.next = self.head
            self.head = element

    def pop(self):
        element = self.head
        self.head = self.head.next
        return element

    def peek(self):
        return self.head

    def search(self, name):
        if self.head is None:
            return "Value Not found"

        element = self.head
        while element:
            if element.value["name"] == name:
                return element.value
            element = element.next
        return "Value Not found"

    def __str__(self):
        if self.head is None:
            return "Stack is empty"
        output =""
        element = self.head
        while element:
            output+=str(element.value)
            output+="\n|\n"
            element = element.next

        return output



myStack = StackDS()

myStack.insert({
    "name":"container1",
    "weight":"600kg",
    "to_go":"Armenia"
})

myStack.insert({
    "name":"container2",
    "weight":"200kg",
    "to_go":"Georgie"
})

myStack.insert({
    "name":"container3",
    "weight":"300kg",
    "to_go":"Russia"
})

myStack.insert({
    "name":"container4",
    "weight":"800kg",
    "to_go":"China"
})



print(myStack.search("container8"))