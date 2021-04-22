class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class BST:

    def __init__(self):
        self.root = None

    def insert(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)

    def _insert(self, current, node):
        if node.value["salary"] < current.value["salary"]:
            if current.left is None:
                current.left = node
            else:
                self._insert(current.left, node)

        else:
            if current.right is None:
                current.right = node
            else:
                self._insert(current.right, node)

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, current):
        '''root, left, right'''
        if current:
            print(current.value)
            self._pre_order(current.left)
            self._pre_order(current.right)

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, current):
        '''left, root, right'''
        if current:
            self._in_order(current.left)
            print(current.value)
            self._in_order(current.right)

    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, current):
        '''left, right, root'''
        if current:
            self._post_order(current.left)
            self._post_order(current.right)
            print(current.value)

    def search(self, salary):
        return self._search(self.root, salary)

    def _search(self, current, salary):
        if current:
            if current.value["salary"] == salary:
                return current.value
            elif salary < current.value["salary"]:
                return self._search(current.left, salary)
            elif salary > current.value["salary"]:
                return self._search(current.right, salary)
        return "Value not found in the BST"

    def delete(self, salary):
        self._delete(self.root, salary, None,None)

    def _delete(self, current, salary, previous, is_left):
        if current:
            if current.value["salary"] == salary:
                if current.left is None and current.right is None: #leaf Node
                    if previous:
                        if is_left:
                            previous.left = None
                        else:
                            previous.right = None
                    else:
                        self.root = None
                elif current.left is None: #One child None (Left is None)
                    if previous:
                        if is_left:
                            previous.left = current.right
                        else:
                            previous.right = current.right
                    else:
                        self.root = current.right
                elif current.right is None: #One child None (Right is None)
                    if previous:
                        if is_left:
                            previous.left = current.left
                        else:
                            previous.right = current.left
                    else:
                        self.root = current.left
                else:# Both left and child nodes are not None
                    min_right = self.get_min_right(current.right)
                    current.value = min_right.value
                    self._delete(current.right, min_right.value["salary"], current, False)


            elif salary < current.value["salary"]:
                return self._delete(current.left, salary,current, True)
            elif salary > current.value["salary"]:
                return self._delete(current.right, salary, current, False)


    def get_min_right(self, current):
        if current.left is None:
            return current
        else:
            return self.get_min_right(current.left)



myBST = BST()
myBST.insert({
    "name":"Andrew",
    "salary":700
})
myBST.insert({
    "name":"Jesica",
    "salary":600
})
myBST.insert({
    "name":"Simon",
    "salary":750
})
myBST.insert({
    "name":"Julie",
    "salary":520
})
myBST.insert({
    "name":"John",
    "salary":670
})
myBST.insert({
    "name":"Brenda",
    "salary":720
})
myBST.insert({
    "name":"Ben",
    "salary":840
})


myBST.in_order()
print("Deleting Brenda====")
myBST.delete(720)
myBST.in_order()

