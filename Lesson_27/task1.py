"""Modify the `depth-first search` to produce strongly connected components"""


class Vertex:

    def __init__(self, key):
        self.key = key  # int
        self.neighbors = {}  # {key: neighbor_vert}
        self.color = 'white'

    def add_neighbor(self, neighbor):
        self.neighbors[neighbor.key] = neighbor

    def __repr__(self):
        return f'V{self.key}'


class Graph:
    """Directed unweighted graph"""

    def __init__(self):
        self.vertices = {}  # key: Vertex(key)
        self.edges = []  # list of tuples (start, dest)

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def add_edge(self, start, dest):
        if start not in self.vertices:
            self.add_vertex(start)
        if dest not in self.vertices:
            self.add_vertex(dest)
        self.vertices[start].add_neighbor(self.vertices[dest])
        self.edges.append((start, dest))

    def dfs(self, start: int, stack=None):
        if stack is None:
            stack = []
        current_vert = self.vertices[start]
        current_vert.color = 'gray'
        for neighbor_key, neighbor in self.vertices[start].neighbors.items():
            if neighbor.color == 'white':
                self.dfs(neighbor_key, stack)
        stack.append(start)
        return stack

    def transpose(self):
        g_t = Graph()
        for i in self.edges:
            g_t.add_edge(i[1], i[0])
        return g_t

    def find_scc(self, start):
        stack = self.dfs(start)
        trans = self.transpose()
        scc = []
        while stack:
            i = stack.pop()
            if trans.vertices[i].color == 'white':
                res = trans.dfs(i)
                scc.append(res)
        return scc

    def __repr__(self):
        return f'Graph: {self.vertices.keys()} | Edges: {self.edges}'


g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print(g.find_scc(0))
