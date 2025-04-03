"""
Módulo que ordena os valores dos adjacentes de cada vértice do mapa.
"""


import numpy as np



class Sort:
    def __init__(self, size):
        self.size = size
        self.array = np.empty(self.size, dtype=int)
        self.last_position = -1

    def list(self):
        if self.last_position == -1:
            print("Vetor vazio.")
        else:
            for index in range(self.last_position + 1):
                print(f"{index} -> {self.array[index]}")

    def insert(self, value):
        if self.last_position == (self.size - 1):
            print("Capacidade maxima atingida")
            return
        
        position = 0
        for position in range(self.last_position + 1):
            if self.array[position] > value:
                break

            if position == self.last_position:
                position += 1

        last_position = self.last_position
        while last_position >= position:
            next_position = last_position + 1
            self.array[next_position] = self.array[last_position]
            last_position -= 1

        self.array[position] = value
        self.last_position += 1

vetor = Sort(5)
vetor.insert(10)
vetor.insert(2)
vetor.insert(0)
vetor.insert(20)
vetor.insert(18)
vetor.insert(10)
vetor.list()
vetor.insert(22)