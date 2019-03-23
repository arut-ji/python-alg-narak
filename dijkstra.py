import heapq
import sys


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {}
        previous = {}
        nodes = []

        for vertex in self.vertices:
            if vertex == start:
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        while nodes:
            smallest = heapq.heappop(nodes)[1]
            if smallest == finish:
                print(str(finish) + ":" + str(distances[finish]), end=' ')
            if distances[smallest] == sys.maxsize:
                break

            for neighbor in self.vertices[smallest]:
                alt = distances[smallest] + self.vertices[smallest][neighbor]
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)

    def __str__(self):
        return str(self.vertices)


g = Graph()
g.add_vertex(1, {2: 8, 3: 5})
g.add_vertex(2, {1: 8, 3: 10, 6: 2, 4: 18})
g.add_vertex(3, {1: 5, 2: 10, 6: 3, 5: 16})
g.add_vertex(4, {2: 18, 7: 4})
g.add_vertex(5, {3: 16, 7: 26})
g.add_vertex(6, {2: 2, 3: 3, 7: 14})
g.add_vertex(7, {4: 4, 6: 14, 5: 26})

for key in g.vertices.keys():
    print(str(key) + ' ', end=' ')
    for destination in g.vertices.keys():
        g.shortest_path(key, destination)
    print()
