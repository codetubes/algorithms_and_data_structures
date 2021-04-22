

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedLists:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_start(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def add_to_end(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        if self.head is None:
            return "The list is empty"
        current = self.head
        self.head = self.head.next
        return current.value

    def search(self, name):

        if self.head.value["name"] == name:
            return self.head.value
        else:
            current = self.head
            while current:
                if current.value["name"] == name:
                    return current.value
                else:
                    current = current.next
        return f"{name} noy found in the list"

    def delete(self, name):
        if self.head.value["name"] == name:
            current = self.head
            self.head = self.head.next
            return current.value
        else:
            current = self.head
            while current.next:
                if current.next.value["name"] == name:
                    current.next = current.next.next
                    return f"{name} value deleted from the list"
                else:
                    current = current.next
        return f"{name} not found in the list"

    def __str__(self):
        current = self.head
        output = "head -> "
        while current:
            output+=current.value["name"]+"->"
            current = current.next
        output +=" tail"
        return output


myList = LinkedLists()
myList.add_to_start({
    "name":"Arman",
    "age":22,
    "country":"Armenia"
})

myList.add_to_start({
    "name":"Andrew",
    "age":34,
    "country":"USA"
})
myList.add_to_start({
    "name":"Andrey",
    "age":18,
    "country":"Russia"
})

myList.add_to_end({
    "name":"Julie",
    "age":24,
    "country":"USA"
})


print(myList)
print(myList.search("Arman"))
print(myList.pop())
print(myList)