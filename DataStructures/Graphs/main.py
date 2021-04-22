
class Node: #vertex
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def add_neighbour(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if node not in self.neighbours:
            self.neighbours.append(node)

class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if node.value not in self.nodes:
            self.nodes[node.value] = node

    def add_edge(self, start, end):
        if start in self.nodes and end in self.nodes:
            for key, node in self.nodes.items():
                if key == start:
                    node.add_neighbour(self.nodes[end])

    def get_paths(self, start, end,path=[]):
        path = path+[start]
        if start == end:
            return [path]

        if start not in self.nodes:
            return []

        paths = []
        for node in self.nodes[start].neighbours:
            if not node.value in path:
                all_paths = self.get_paths(node.value, end, path)
                for p in all_paths:
                    paths.append(p)
        return paths


    def get_shortest_path(self, start, end, path = []):
        path = path+[start]
        if start == end:
            return path

        if start not in self.nodes:
            return None

        shortestPath = None
        for node in self.nodes[start].neighbours:
            if node.value not in path:
                sp = self.get_shortest_path(node.value, end, path)
                if shortestPath is None or len(shortestPath) > len(sp):
                    shortestPath = sp
        return shortestPath







    def __str__(self):
        output = ""
        for key, node in self.nodes.items():
            output+=("{0}: {1}\n".format(key, [n.value for n in node.neighbours]))
        return output


myGraph = Graph()
myGraph.add_node("USA")
myGraph.add_node("Germany")
myGraph.add_node("Russia")
myGraph.add_node("Georgia")
myGraph.add_node("Armenia")
print("Creating edges")
myGraph.add_edge("USA", "Germany")
myGraph.add_edge("USA", "Russia")
myGraph.add_edge("Germany", "Russia")
myGraph.add_edge("Germany", "Georgia")
myGraph.add_edge("Russia", "Georgia")
myGraph.add_edge("Georgia", "Armenia")
print(myGraph)
print(myGraph.get_paths("USA", "Georgia"))
print(myGraph.get_shortest_path("USA", "Georgia"))

