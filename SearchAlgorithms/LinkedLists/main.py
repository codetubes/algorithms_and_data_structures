
"""Linke Lists"""


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, x):
        '''append new element to the end for the list'''
        if not isinstance(x, Node):
            x = Node(x)

        if self.head == None:
            self.head = x
        else:
            self.tail.next = x

        self.tail = x

    def prepend(self,x):
        '''Add an element to the beginning of the list'''
        if not isinstance(x, Node):
            x = Node(x)

        if self.head is None:
            self.tail = x
        else:
            x.next = self.head

        self.head = x

    def search(self,x):
        '''Search and return index'''
        if self.head == None:
            return None
        else:
            current = self.head
            index = 0
            while current != None:
                if current.data == x:
                    return f"Number {x} found at index {index}"
                index +=1
                current = current.next
            return None

    def remove(self, x):
        """Remove element with provided value"""

        current = self.head
        while current and  current.next != None:
            if current.next.data == x:
                next_node = current.next.next
                current.next = current.next.next
                current = next_node
            else:
                current = current.next

    def reverse(self, current, previous):
        #[8->3->10->4]
        if self.head == None:
            return None
        elif current.next == None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.reverse(next, current)





    def __str__(self):
        '''Print the list'''
        if self.head is None:
            return "[]"
        else:
            output = ""
            current = self.head
            while current != None:
                output += f"{current.data}->"
                current = current.next

            output="["+output[:-2]+"]"
            return output

myList = LinkedList()
myList.append(10)
myList.append(4)
myList.prepend(3)
myList.prepend(8)
print(myList)
myList.reverse(myList.head, None)
print(myList)

