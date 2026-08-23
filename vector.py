# Criar uma classe Vector onde terá atributos contendo a dimensões daquele elemento.
# Ele que me contará qual é a dimensão daquela matriz.

class Vector:
    def __init__(self, dim, elements):

        # < 'List' vai converter o objeto em listas
        self.elements = list(elements)
        # <- 'len' Irá contar a quantidade de elementos
        self.dim = len(self.elements)

        # Vai vê se o valor está na lista e garante pegar o valor guardado
        # Uma forma de conseguir pegar posições que esteja em 0, 1 e 2.

    def get(self, i):

        if 0 <= i < self.dim:
            return self.elements[i]
        else:
            raise IndexError(f"Alcance ERRADO´{self.dim}.")
    # Basicamente para adicionar um valor novo na dimensão escolhida

    def set(self, i, value):

        if 0 <= i < self.dim:
            self.elements[i] = value
            return self.elements
        else:
            raise IndexError("O valor não foi definido {i}")
   # Construído para evitar <__main__.Vector object at 0x00000145272182F0>

    def __str__(self):

        return f"Vetor({self.dim}): {self.elements}"


Matriz = Vector(3, [[3, 1, 5],  # <- Matriz personalizada criada
                    [7, 10, 6],
                    [8, 4, 2]])

# Printar matriz original
print("Matriz Original:", Matriz)
# <- de 0 à 2 você vai escolher a posição dessa dimensão
# 1x1 primeira dimensação, 2x2 segunda dimensao, 3x3 terceira dimensao
matrizposicao = Matriz.get(1)
print("Posicao guardada: ", matrizposicao)

# Declaro uma variável e vou adicionar [1, 1, 1 ] na linha escolhida que '1'
matrizadicionar = Matriz.set(1, [1, 1, 1])
print("Posicao adicionada:", matrizadicionar)

# Linha para destacar a dimensao escolhida
dimensaoescolhidaatual = Matriz.get(1)
print("A dimensação que foi escolhida: ", dimensaoescolhidaatual)
