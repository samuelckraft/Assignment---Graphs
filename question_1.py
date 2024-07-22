#Task 1
import heapq
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

#Task 2  
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0

        pq = [(0, start)] #priority queue of (distance, vertex)

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances

#Task 3
graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_edge(1, 2, 2)
graph.add_edge(2, 3, 5)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 1, 6)

distances = graph.dijkstra(3)
print("Shortest distance from vertex 1:", distances)


#Task 4
#Time complexity = O((V + E) log V) where V is the number of vertices and E is the number of edges