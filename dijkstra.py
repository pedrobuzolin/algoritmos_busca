DISTANCE = 0
PREDECESSOR = 1
INFINITY = float("inf")

graph = {
    "A": {"B": 4, "C": 3},
    "B": {"A": 4, "C": 5, "D": 2},
    "C": {"A": 3, "B": 5, "D": 1, "E": 3},
    "D": {"B": 2, "C": 1, "E": 4},
    "E": {"C": 3, "D": 4} 
}

table = {
    "A": [0, None],
    "B": [INFINITY, None],
    "C": [INFINITY, None],
    "D": [INFINITY, None],
    "E": [INFINITY, None]
}

def get_shortest_distance(table: dict, vertex: str) -> int:
    return table[vertex][DISTANCE]

def set_shortes_distance(table: dict, vertex: str, distance: int):
    table[vertex][DISTANCE] = distance

def set_predecessor(table: dict, vertex: str, predecessor: str):
    table[vertex][PREDECESSOR] = predecessor

def get_distance(graph: dict, first_vertex: str, second_vertex: str):
    return graph[first_vertex][second_vertex]

def get_next_vertex(table: dict, visited: list):
    unvisited = list(
        set(
            table.keys()
        ).difference(visited)
    )

    min_vertex = unvisited[0]
    min_distance = table[unvisited[0]][DISTANCE]

    for vertex in unvisited:
        if table[vertex][DISTANCE] < min_distance:
            min_vertex = vertex
            min_distance = table[vertex][DISTANCE]

    return min_vertex

def find_shortest_path(graph: dict, table: dict, origin: str = "A"):
    visited = []
    current = origin
    start = origin

    while True:
        adjacent_vertex = graph[current]

        if set(adjacent_vertex).issubset(set(visited)):
            ...
        else:
            unvisited = set(adjacent_vertex).difference(set(visited))

            for vertex in unvisited:
                distance_from_start = get_shortest_distance(table, vertex)

                if distance_from_start == INFINITY and current == start:
                    total_distance = get_distance(graph, vertex, current)
                else:
                    total_distance = get_shortest_distance(table, current)
                    total_distance += get_distance(graph, current, vertex)
                
                if total_distance < distance_from_start:
                    set_shortes_distance(table, vertex, total_distance)
                    set_predecessor(table, vertex, current)
        
        visited.append(current)

        if len(visited) == len(table.keys()):
            break
        
        current = get_next_vertex(table, visited)

    return table

def show_path(table: dict, origin: str = "A", destiny: str = "E"):
    path = []
    vertex = destiny

    while vertex is not None:
        path.append(vertex)
        vertex = table[vertex][PREDECESSOR]

        if vertex == origin:
            path.append(origin)
            break
    
    return path[::-1]

#def show_path(destino, solucoes):
#    rota = []
#    atual = destino

#    while atual is not None:
#        rota.append(solucoes[atual][1])
#        atual = solucoes[atual][1]
    
#    return path[::-1]



result = find_shortest_path(graph, table)
print(result)  

path = show_path(table)
print(path)