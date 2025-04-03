"""
Exemplo de Greed Search.
"""

from graph import Graph
from sort import Sort

class Routes:
    def __init__(self, target):
        self.target = target
        self.found = False

    def search(self, current):
        """
        Método que busca a rota até o target
        """
        print(f"\nAtual: {current.label}")
        current.visited = True

        if current == self.target:
            self.found = True
        else:
            routes_sorted = Sort(len(current.adjacent))

            for adjacent in current.adjacent:
                adjacent.vertex.visited = True
                routes_sorted.insert(adjacent.vertex)
            
            routes_sorted.list()
            
            if routes_sorted.cities[0]:
                self.search(routes_sorted.cities[0])

if __name__ == "__main__":
    map = Graph()
    gps = Routes(map.bucarest)
    gps.search(map.arad)