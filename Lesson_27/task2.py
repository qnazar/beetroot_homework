"""Using breadth-first search write an algorithm that can determine the shortest path
from each vertex to every other vertex. This is called the all-pairs shortest path problem."""

# Case 1: non-weighted directed graph ----------------------------------------------------------------------------------


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = set()
        self.distance = 0

    def connect_to(self, neighbor):
        self.neighbors.add(neighbor)

    def __repr__(self):
        return f'V{self.key}'


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_edge(self, from_, to_):
        if from_ not in self.vertices:
            self.vertices[from_] = Vertex(from_)
        if to_ not in self.vertices:
            self.vertices[to_] = Vertex(to_)
        self.vertices[from_].connect_with(self.vertices[to_])
        self.edges.append((from_, to_))

    def bfs(self, start):
        queue = []
        visited = []
        start = self.vertices[start]
        start.distance = 0
        queue.append(start)
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in queue and neighbor not in visited:
                    neighbor.distance = current.distance + 1
                    queue.append(neighbor)
            visited.append(current)
        return {x: x.distance for x in visited}

    def all_pairs(self):
        for i in range(len(self.vertices)):
            print(f'Paths from V{i} - ', self.bfs(i))


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(0, 3)
# g.add_edge(1, 2)
# g.add_edge(2, 4)
# g.add_edge(3, 4)
# g.add_edge(4, 5)
# g.add_edge(2, 5)
# g.add_edge(5, 6)
# g.add_edge(1, 6)
#
# g.all_pairs()


# Case 2: non-weighted undirected graph --------------------------------------------------------------------------------

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = set()
        self.distance = 0

    def connect_with(self, neighbor):
        self.neighbors.add(neighbor)
        neighbor.neighbors.add(self)

    def __repr__(self):
        return f'V{self.key}'


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.vertices[v1] = Vertex(v1)
        if v2 not in self.vertices:
            self.vertices[v2] = Vertex(v2)
        self.vertices[v1].connect_with(self.vertices[v2])
        self.edges.append((v1, v2))
        self.edges.append((v2, v1))

    def bfs(self, start):
        queue = []
        visited = []
        start = self.vertices[start]
        start.distance = 0
        queue.append(start)
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in queue and neighbor not in visited:
                    neighbor.distance = current.distance + 1
                    queue.append(neighbor)
            visited.append(current)
        return {x: x.distance for x in visited}

    def all_pairs(self):
        for i in range(len(self.vertices)):
            print(f'Paths from V{i} - ', self.bfs(i))


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(0, 3)
# g.add_edge(1, 2)
# g.add_edge(2, 4)
# g.add_edge(3, 4)
# g.add_edge(4, 5)
# g.add_edge(2, 5)
# g.add_edge(5, 6)
# g.add_edge(1, 6)
#
# g.all_pairs()

# Case 3: weighted directed graph with all positive arches -------------------------------------------------------------
from math import inf

class Vertex:

    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.distance = inf

    def add_neighbor(self, neigh, weight):
        self.neighbors[neigh] = weight

    def __repr__(self):
        return f'V{self.key}'


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_edge(self, from_, to_, weight):
        if from_ not in self.vertices:
            self.vertices[from_] = Vertex(from_)
        if to_ not in self.vertices:
            self.vertices[to_] = Vertex(to_)
        self.vertices[from_].add_neighbor(self.vertices[to_], weight)
        self.edges[(from_, to_)] = weight

    def dijkstra(self, start):
        queue = []
        visited = []
        start = self.vertices[start]
        for vertex in self.vertices.values():
            vertex.distance = inf
        start.distance = 0
        queue.append(start)
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in queue and neighbor not in visited:
                    queue.append(neighbor)
                    new_distance = current.distance + self.edges[(current.key, neighbor.key)]
                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
            visited.append(current)
        return {x: x.distance for x in visited}

    def all_pairs(self):
        for vertex in self.vertices:
            print(f'Paths from {vertex} - ', self.dijkstra(vertex))

    def __repr__(self):
        return f'Graph V - {self.vertices}, E - {self.edges}'


# g = Graph()
# g.add_edge(0, 1, 4)
# g.add_edge(0, 2, 3)
# g.add_edge(1, 2, 5)
# g.add_edge(1, 3, 2)
# g.add_edge(2, 3, 7)
# g.add_edge(3, 4, 2)
# g.add_edge(4, 1, 4)
# g.add_edge(4, 0, 4)
# g.add_edge(4, 5, 6)
#
# g.all_pairs()

# Case 4: weighted undirected graph with all positive arches -----------------------------------------------------------

class Vertex:
    def __init__(self, key):
        self.key = key
        self.distance = inf
        self.neighbors = {}

    def connect_with(self, neighbor, weight):
        self.neighbors[neighbor] = weight
        neighbor.neighbors[self] = weight

    def __repr__(self):
        return f'V{self.key}'


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_edge(self, v1, v2, weight):
        if v1 not in self.vertices:
            self.vertices[v1] = Vertex(v1)
        if v2 not in self.vertices:
            self.vertices[v2] = Vertex(v2)
        self.vertices[v1].connect_with(self.vertices[v2], weight)
        self.edges[(v1, v2)] = weight
        self.edges[(v2, v1)] = weight

    def dijkstra(self, start):
        queue = []
        visited = []
        start = self.vertices[start]
        for vertex in self.vertices.values():
            vertex.distance = inf
        start.distance = 0
        queue.append(start)
        while queue:
            current = queue.pop(0)
            visited.append(current)
            for neighbor in sorted(current.neighbors, key=current.neighbors.get):
                if neighbor not in visited:
                    queue.append(neighbor)
                    new_distance = current.distance + self.edges[(current.key, neighbor.key)]
                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
        return {x: x.distance for x in visited}

    def all_pairs(self):
        for vertex in self.vertices:
            print(f'Paths from {vertex} - ', self.dijkstra(vertex))


# g = Graph()
# g.add_edge(0, 1, 4)
# g.add_edge(1, 2, 8)
# g.add_edge(2, 3, 7)
# g.add_edge(3, 4, 9)
# g.add_edge(4, 5, 10)
# g.add_edge(5, 2, 4)
# g.add_edge(5, 3, 14)
# g.add_edge(5, 6, 2)
# g.add_edge(6, 7, 1)
# g.add_edge(6, 8, 6)
# g.add_edge(7, 1, 11)
# g.add_edge(7, 8, 7)
# g.add_edge(7, 0, 8)
# g.add_edge(8, 2, 2)
#
# g.all_pairs()
