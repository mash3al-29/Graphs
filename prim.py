import heapq


def initialize(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    return distances, predecessors


def prim(graph, start):
    visited = set()
    min_heap = [(0, None, start)]
    parents = {start: None}
    # mst_edges = []
    while len(visited) != len(graph):
        weight, parent, vertex = heapq.heappop(min_heap)
        if vertex not in visited:
            visited.add(vertex)
            parents[vertex] = parent
            for edge in graph[vertex]:
                heapq.heappush(min_heap, (edge[1], vertex, edge[0]))
    return parents


graph_ = dict()


def add_edge(edge):
    if edge[0] not in graph_:
        graph_[edge[0]] = []
    if edge[1] not in graph_:
        graph_[edge[1]] = []
    graph_[edge[0]].append([edge[1], edge[2]])
    graph_[edge[1]].append([edge[0], edge[2]])


# def make_graph():
#     add_edge(('a', 'b', 9))
#     add_edge(('a', 'c', 5))
#     add_edge(('a', 'd', 2))
#
#     add_edge(('b', 'e', 5))
#     add_edge(('b', 'd', 6))
#
#     add_edge(('c', 'd', 4))
#     add_edge(('c', 'e', 5))
#
#     add_edge(('d', 'e', 4))

def make_graph():
    add_edge(('a', 'b', 4))
    add_edge(('a', 'h', 8))

    add_edge(('b', 'h', 11))
    add_edge(('b', 'c', 8))

    add_edge(('c', 'i', 2))
    add_edge(('c', 'f', 4))
    add_edge(('c', 'd', 7))

    add_edge(('i', 'h', 7))
    add_edge(('i', 'g', 6))

    add_edge(('h', 'g', 1))

    add_edge(('g', 'f', 2))

    add_edge(('d', 'e', 9))
    add_edge(('d', 'f', 14))

    add_edge(('f', 'e', 10))


make_graph()
# print(graph_)
print(prim(graph_, 'e'))
