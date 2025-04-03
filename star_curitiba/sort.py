import numpy as np

class Sort:
    def __init__(self, size):
        self.size = size
        self.cities = np.empty(self.size, dtype=object)
        self.last_position = -1

    def list(self):
        if self.last_position == -1:
            print("Vetor vázio.")
        else:
            for index in range(self.last_position + 1):
                print(f"{index} -> {self.cities[index].vertex.label}")
                print(f"\t KM: {self.cities[index].cost}")
                print(f"\t Heurística: {self.cities[index].vertex.target_distance}")
                print(f"\t Star: {self.cities[index].star_distance}\n")
    
    def insert(self, value):
        if self.last_position == (self.size - 1):
            print("Capacidade máxima atingida")
            return

        position = 0
        for position in range(self.last_position + 1):
            if self.cities[position].star_distance > value.star_distance:
                break

            if position == self.last_position:
                position += 1

        last_postion = self.last_position
        while last_postion >= position:
            next_position = last_postion + 1
            self.cities[next_position] = self.cities[last_postion]
            last_postion -= 1
        
        self.cities[position] = value
        self.last_position += 1