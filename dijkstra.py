import heapq


def initialize(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    return distances, predecessors


def get_all_shortest_paths(source, predecessors):
    all_paths = {}
    for destination in predecessors:
        if destination == source:
            continue
        path = []
        current_vertex = destination
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = predecessors[current_vertex]
        path.reverse()
        all_paths[destination] = path
    return all_paths


def dijkstra(graph, start):
    distances, predecessors = initialize(graph, start)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance <= distances[current_vertex]:
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))
    all_shortest_paths = get_all_shortest_paths(0, predecessors)
    return distances, predecessors, all_shortest_paths


graph = {
    0: [(1, 10), (2, 5)],
    1: [(2, 2), (3, 1)],
    2: [(3, 9), (4, 2), (1, 3)],
    3: [(4, 4)],
    4: [(3, 6), (0, 7)],
}

distances, predecessors, all_shortest_paths = dijkstra(graph, 0)
for destination, shortest_path in all_shortest_paths.items():
    print("Shortest path from", 0, "to", destination, ":", shortest_path)

print("Distances:", distances)
print("Predecessors:", predecessors)
