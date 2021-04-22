

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.tail = None
        self.head = None

    def add_to_start(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
            self.tail = value
        else:
            value.next = self.head
            self.head = value

    def add_to_end(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value

    def pop(self):
        if self.head is None:
            return None

        current_element = self.head
        self.head = self.head.next
        return current_element.value

    def search(self, name):
        current_element = self.head
        while current_element:
            if current_element.value["name"] == name:
                return current_element.value
            current_element = current_element.next

        return "Element not found in the list"

    def delete(self, value):
        current_element = self.head
        if current_element.value["name"] == self.head.value["name"]:
            self.head = self.head.next
        else:
            while current_element:
                if current_element.next is not None:
                    if current_element.next.value["name"] == value:
                        current_element.next = current_element.next.next

                current_element = current_element.next

    def __str__(self):
        current_element = self.head
        output = ""
        while current_element:
            output+=(str(current_element.value)+"->")
            current_element = current_element.next

        return output



myList = LinkedList()
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
myList.delete("Andrey")
print(myList)