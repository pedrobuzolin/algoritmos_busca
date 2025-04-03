"""
Módulo que define o mapa da Romênia no formato de grafo, considerando a heurística
"""


class Vertex:
    """
    Classe que define um vértice, como uma cidade tendo seus adjacentes (rotas), e considerando a heurística 
    (distância em linha reta do vértice até Bucareste).
    """

    def __init__(self, label: str, target_distance: int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []
        self.visited = False
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def list_adjacent(self):
        for adjacent in self.adjacent:
            print(f"{adjacent.vertex.label} - {adjacent.cost}")


class Adjacent:
    def __init__(self, vertex: Vertex, cost: int):
        self.vertex = vertex
        self.cost = cost
        self.star_distance = vertex.target_distance + self.cost


class Graph:
    arad = Vertex("Arad", 366)
    zerind = Vertex("Zerind", 374)
    oradea = Vertex("Oradea", 380)
    sibiu = Vertex("Sibiu", 253)
    timisoara = Vertex("Timisoara", 329)
    lugoj = Vertex("Lugoj", 244)
    mehadia = Vertex("Mehadia", 241)
    dobreta = Vertex("Dobreta", 242)
    craiova = Vertex("Craiova", 160)
    rimnicu = Vertex("Rimnicu Vilcea", 193)
    fagaras = Vertex("Fagara", 176)
    pitesti = Vertex("Pitesti", 100)
    bucarest = Vertex("Bucarest", 0)
    giurgiu = Vertex("Giurgiu", 77)

    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(timisoara, 118))
    arad.add_adjacent(Adjacent(sibiu, 140))

    zerind.add_adjacent(Adjacent(oradea, 71))
    zerind.add_adjacent(Adjacent(arad, 75))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(arad, 140))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))
    sibiu.add_adjacent(Adjacent(fagaras, 99))

    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    lugoj.add_adjacent(Adjacent(timisoara, 111))
    lugoj.add_adjacent(Adjacent(mehadia, 70))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(craiova, 120))
    dobreta.add_adjacent(Adjacent(mehadia, 75))

    craiova.add_adjacent(Adjacent(dobreta, 120))
    craiova.add_adjacent(Adjacent(pitesti, 138))
    craiova.add_adjacent(Adjacent(rimnicu, 146))

    rimnicu.add_adjacent(Adjacent(craiova, 146))
    rimnicu.add_adjacent(Adjacent(sibiu, 80))
    rimnicu.add_adjacent(Adjacent(pitesti, 97))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucarest, 211))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(craiova, 138))
    pitesti.add_adjacent(Adjacent(bucarest, 101))

    bucarest.add_adjacent(Adjacent(pitesti, 101))
    bucarest.add_adjacent(Adjacent(fagaras, 211))
    bucarest.add_adjacent(Adjacent(giurgiu, 90))