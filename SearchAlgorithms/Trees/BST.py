

class Node():

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f" {self.data} "

class BST():


    def __init__(self):
        self.root = None


    def insert(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.root == None:
            self.root = x
        else:
            self._insert(self.root, x)

    def _insert(self, current, x):
        if current.data > x.data:
            if current.left_child is None:
                current.left_child = x
            else:
                self._insert(current.left_child, x)
        else:
            if current.right_child is None:
                current.right_child = x
            else:
                self._insert(current.right_child, x)

    def in_order(self):
        self._in_order(self.root)
        print("")

    def _in_order(self, current):
        if current:
            self._in_order(current.left_child)
            print(current.data, end=" ")
            self._in_order(current.right_child)

    def pre_order(self):
        '''root, left, right'''
        self._pre_order(self.root)
        print("")

    def _pre_order(self, current):
        if current:
            print(current.data, end=" ")
            self._pre_order(current.left_child)
            self._pre_order(current.right_child)

    def post_order(self):
        '''left, right, root'''
        self._post_order(self.root)
        print("")

    def _post_order(self, current):
        if current:
            self._post_order(current.left_child)
            self._post_order(current.right_child)
            print(current.data, end=" ")

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, current, key):
        if current:
            if current.data == key:
                return "Element exist in tree"
            elif current.data > key:
                return self._find_val(current.left_child, key)
            else:
                return self._find_val(current.right_child, key)


        return "Key not found"


    def delete_val(self, key):
        self._delete_val(self.root,None, None,  key)

    def _delete_val(self, curr,prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    pass

                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child

                elif curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child


            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            else:
                self._delete_val(curr.right_child,curr, False, key)
        else:
            print(f"{key} not found in tree")




tree = BST()

tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")

tree.delete_val("H")
#tree.in_order()
#tree.pre_order()
#tree.post_order()
