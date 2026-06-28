class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, name):
        if name not in self.adjacency_list:
            self.adjacency_list[name] = {}

    def add_edge(self, a, b, weight):
        self.add_node(a)
        self.add_node(b)
        self.adjacency_list[a][b] = weight
        self.adjacency_list[b][a] = weight

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, {})

    def remove_node(self, name):
        self.adjacency_list.pop(name, None)
        for neighbors in self.adjacency_list.values():
            neighbors.pop(name, None)