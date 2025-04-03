
class Vertex:
    def __init__(self, label: str, target_distance: int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []
        self.visited = False

    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)
    
    def list_adjacente(self):
        for adjacent in self.adjacent:
            print(f"{adjacent.vertex.label} - {adjacent.cost}")

class Adjacent:
    def __init__(self, vertex: Vertex, cost: int):
        self.vertex = vertex
        self.cost = cost

class Curitiba:
    curitiba = Vertex("Curitiba", 0)
    porto_uniao = Vertex("Porto União", 203)
    paulo_frontin = Vertex("Paulo Frontin", 172)
    canoinhas = Vertex("Canoinhas", 141)
    tres_barras = Vertex("Três Barras", 131)
    sao_mateus = Vertex("São Mateus do Sul", 123)
    irati = Vertex("Irati", 139)
    palmeira = Vertex("Palmeira", 59)
    mafra = Vertex("Mafra", 94)
    campo_largo = Vertex("Campo Largo", 27)
    balsa_nova = Vertex("Balsa Nova", 41)
    lapa = Vertex("Lapa", 74)
    tijucas_sul = Vertex("Tijucas do Sul", 56)
    araucaria = Vertex("Araucaria", 23)
    sao_jose = Vertex("São Jose dos Pinhais", 13)
    contenda = Vertex("Contenda", 39)

    porto_uniao.add_adjacent(Adjacent(paulo_frontin, 46))
    porto_uniao.add_adjacent(Adjacent(sao_mateus, 87))
    porto_uniao.add_adjacent(Adjacent(canoinhas, 78))

    paulo_frontin.add_adjacent(Adjacent(porto_uniao, 46))
    paulo_frontin.add_adjacent(Adjacent(irati, 75))

    irati.add_adjacent(Adjacent(paulo_frontin, 75))
    irati.add_adjacent(Adjacent(sao_mateus, 57))
    irati.add_adjacent(Adjacent(palmeira, 75))

    palmeira.add_adjacent(Adjacent(irati, 75))
    palmeira.add_adjacent(Adjacent(sao_mateus, 77))
    palmeira.add_adjacent(Adjacent(campo_largo, 55))

    campo_largo.add_adjacent(Adjacent(palmeira, 55))
    campo_largo.add_adjacent(Adjacent(balsa_nova, 22))
    campo_largo.add_adjacent(Adjacent(curitiba, 29))

    sao_mateus.add_adjacent(Adjacent(porto_uniao, 87))
    sao_mateus.add_adjacent(Adjacent(irati, 57))
    sao_mateus.add_adjacent(Adjacent(tres_barras, 43))
    sao_mateus.add_adjacent(Adjacent(lapa, 60))
    sao_mateus.add_adjacent(Adjacent(palmeira, 77))

    tres_barras.add_adjacent(Adjacent(sao_mateus, 43))
    tres_barras.add_adjacent(Adjacent(canoinhas, 12))

    canoinhas.add_adjacent(Adjacent(tres_barras, 12))
    canoinhas.add_adjacent(Adjacent(porto_uniao, 78))
    canoinhas.add_adjacent(Adjacent(mafra, 66))

    mafra.add_adjacent(Adjacent(canoinhas, 66))
    mafra.add_adjacent(Adjacent(lapa, 57))
    mafra.add_adjacent(Adjacent(tijucas_sul, 99))

    tijucas_sul.add_adjacent(Adjacent(mafra, 99))
    tijucas_sul.add_adjacent(Adjacent(sao_jose, 49))

    sao_jose.add_adjacent(Adjacent(tijucas_sul, 49))
    sao_jose.add_adjacent(Adjacent(curitiba, 15))

    lapa.add_adjacent(Adjacent(mafra, 57))
    lapa.add_adjacent(Adjacent(sao_mateus, 60))
    lapa.add_adjacent(Adjacent(contenda, 26))

    contenda.add_adjacent(Adjacent(lapa, 26))
    contenda.add_adjacent(Adjacent(balsa_nova, 19))
    contenda.add_adjacent(Adjacent(araucaria, 18))

    araucaria.add_adjacent(Adjacent(contenda, 18))
    araucaria.add_adjacent(Adjacent(curitiba, 37))

    balsa_nova.add_adjacent(Adjacent(campo_largo, 22))
    balsa_nova.add_adjacent(Adjacent(contenda, 19))
    balsa_nova.add_adjacent(Adjacent(curitiba, 51))

    curitiba.add_adjacent(Adjacent(campo_largo, 29))
    curitiba.add_adjacent(Adjacent(balsa_nova, 51))
    curitiba.add_adjacent(Adjacent(araucaria, 37))
    curitiba.add_adjacent(Adjacent(sao_jose, 15))
