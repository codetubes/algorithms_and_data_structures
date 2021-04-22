

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.head == None:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value
    def pop(self):
        if self.head is None:
            return "List is empty"
        else:
            current = self.head
            self.head = self.head.next
            return current.value

    def peek(self):
        if self.head is None:
            return "List is empty"
        else:
            return self.head.value

    def search(self, value):
        if self.head is None:
            return "List is empty"
        else:
            current = self.head
            while current:
                if current.value == value:
                    return f"{value} found in list"
                current = current.next

            return f"{value} not found in the list"

    def __str__(self):
        output = "head -> "
        if self.head is None:
            return "List is empty"
        else:
            current = self.head
            while current:
                output+=f"{current.value} ->"
                current = current.next

        output+=" tail"
        return output

myList = Queue()
myList.add("Arman")
myList.add("John")
myList.add("Julie")
myList.add("Simon")
print(myList)
print(myList.peek())
print(myList.search("Andrew"))

