

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def insert(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
        else:
            value.next = self.head
            self.head = value



    def pop(self):
        current_element = self.head
        self.head = self.head.next
        return current_element

    def peek(self):
        return self.head

    def search(self, name):
        if self.head is None:
            return "Value not found"

        current_element = self.head
        while current_element:
            if current_element.value["name"] == name:
                return current_element.value
            current_element = current_element.next

        return "Value not found"

    def __str__(self):
        if self.head is None:
            return "Stack is empty"

        output = ""
        current_element = self.head
        while current_element:
            output+=str(current_element.value)
            output+="\n|\n"
            current_element = current_element.next

        return output

myStack = Stack()
myStack.insert(
    {
        "name":"container1",
        "weight":"600kg",
        "to_go":"Armenia"
    }
)

myStack.insert(
    {
        "name":"container2",
        "weight":"300kg",
        "to_go":"Georgia"
    }
)

myStack.insert(
    {
        "name":"container3",
        "weight":"200kg",
        "to_go":"Russia"
    }
)

myStack.insert(
    {
        "name":"container4",
        "weight":"800kg",
        "to_go":"China"
    }
)

#print(myStack)
print(myStack.search("container8"))