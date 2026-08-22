# Linha 1 = row
# [] = linhas
# 1, 2, 3 = elementos
class Matrix:
   # Foi utilizado self para indicar colunas e linhas.

    def __init__(self, rows, cols, elements):
        self.rows = rows  # quantidade de Linhas
        self.cols = cols  # quantidade de Colunas
        # Elementos da minha escolha colocado
        self.elements = elements
        self.matriz = [[elements[i][j] for j in range(
            # quantidade de linhas e colunas que essa matriz irá contar
            cols)] for i in range(rows)]

        # Método get vai receber os parâmetros da linha i e j de uma posicao
        # e irá retornar o valor guardado nesta posição
    def get(self, row, col):
        # Basicamente o uso de if para não ir fora do limite
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matriz[row][col]
        # Senão vai retornar posicação fora de limite
        else:
            return "Posicao fora do limite da matriz"
   # Antes usamos o método get para pegar um valor escolhido e agora vou modificar
   # o valor especifico usando método set.

    def set(self, row, col, value):

        # Aqui eu vou criar uma segurança para dizer que houve uma escolha errada
        # quando escolhe a posicao inexiste

        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matriz[row][col] = value
            return True
        print("Botou posicao errada")
        return False


# Variável matrix que recebe Matrix que é a minha classe, nela é a quantidade de linhas(rows) e colunas(cols)
# Basicamente estou dizendo que na classe vai carregar a matriz da minha escolha e a quantidade
# de linhas ou colunas que ela vai ter representado por 3,3


matrix = Matrix(3, 3,  # < Quantidade de linhas e colunas que você deseja
                [[3, 5, 6],  # < Matriz aleatória escolhida
                 [2, 6, 2],
                 [2, 5, 2]])

print("Matriz inicial:")
print(matrix.matriz)

# Usando método get, vamos pegar um valor que está em uma coluna e linha
# Criamos uma variável valor e aplicamos um método get para escolher a linha e coluna
matrix.valor = matrix.get(1, 2)
print("valor da posição e linha escolhida:", matrix.valor)

# Usando o método set, vamos pegar o valor que desejamos e vamos modifica-los criando uma variável

# <- basicamente, olha pc, eu quero colocar o valor 10 na coluna 1 e linha 2
matrix.set(1, 2, 10)
print("Matriz modificada:")
print(matrix.matriz)

matrix.valor = matrix.get(1, 2)
print("\n")
print("valor novo inserido:", matrix.valor)
