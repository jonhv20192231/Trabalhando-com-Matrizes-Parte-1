
class Matrix:
   
    def __init__(self, rows, cols, elements):
        self.rows = rows  
        self.cols = cols 
        # Elementos da minha escolha colocado
        self.elements = elements
        self.matriz = [[elements[i][j] for j in range(
      
            cols)] for i in range(rows)]

Foi criado uma classe Matriz onde irá efetuar os cálculos, nisso criei o self para dar
atributos praquela matriz, onde ela vai ter colunas, linhas e elementos

self. matriz é onde vai dar o tamanho da matriz que será conta de 0, 1 e 2

def get(self, row, col):
        
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matriz[row][col]
        
        else:
            return "Posicao fora do limite da matriz"

Basicamente pra pegar um valor específico que está em uma linha e coluna

Foi utilizado o if else para avisar caso coloque valor errado

def set (self, row, col, value):


        if 0 <= row <self.rows and 0 <=col < self.cols:
            self.matriz[row][col] = value 
            return True
        print("Botou posicao errada")
        return False

Esse método set é usado para inserir um novo 'valor' na linha e coluna escolhida

matrix = Matrix(3, 3,  # 
                [[3, 5, 6],  
                 [2, 6, 2],
                 [2, 5, 2]])

Variável matrix que recebe uma matriz que vai de escolha do usuário de qual ordem ele deseja trabalhar


print("Matriz inicial:")
print(matrix.matriz)

Printa a matriz inicial

matrix.valor = matrix.get(1, 2)
print("valor da posição e linha escolhida:", matrix.valor)


Basicamente para eu escolher a posição específica de onde está o número, no caso 2

matrix.set(1, 2, 10) 
print("Matriz modificada:")
print(matrix.matriz) 


Set segue a mesma lógica do get, mas no caso ele vai inserir um novo valor

