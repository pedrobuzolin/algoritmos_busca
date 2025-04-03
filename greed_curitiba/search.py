from graph import Curitiba
from sort import Sort

class Routes:
    def __init__(self, target):
        self.target = target
        self.found = False

    def search(self, current):
        print(f"Atual: {current.label}")
        current.visited = True

        if current == self.target:
            self.found = True
        else:
            routes_sorted = Sort(len(current.adjacent))

            for adjacent in current.adjacent:
                adjacent.vertex.viseted = True
                routes_sorted.insert(adjacent.vertex)

            routes_sorted.list()

            if routes_sorted.cities[0]:
                self.search(routes_sorted.cities[0])

if __name__ == "__main__":
    map = Curitiba()
    gps = Routes(map.curitiba)
    gps.search(map.porto_uniao)