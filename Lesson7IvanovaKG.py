class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = '\n'
        for row in self.matrix:
            for el in row:
                my_str += f'{el:>10}'
            my_str += '\n'
        return my_str
    def __add__(self, other):
        add = []
        if len(self.matrix) != len(other.matrix):
            print('Please check matrices dimensions')
            return
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                print('Please check matrices dimensions')
                return None
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            add.append(row)

        return Matrix(add)
my_m1 = Matrix([[1, 5, 3, 6], [0, 5, 2, 7], [9, 67, 34, 91]])
print(f'my_m1 = {my_m1}')
my_m2 = Matrix([[2, 5, 1, 8], [0, 54, 2, 77], [23, 3, 75, 8]])
print(f'my_m2 = {my_m2}')
print(f'my_m1 + my_m2 = {my_m1 + my_m2}')


from abc import ABC, abstractmethod


class Garment(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Garment):
    def __init__(self, param):
        super().__init__(param)
        print(f'There is a new coat with size {self.param}')

    @property
    def get_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Garment):
    def __init__(self, param):
        super().__init__(param)
        print(f'There is a new suit with height {self.param}')

    @property
    def get_consumption(self):
        return round(self.param * 2 + 0.3, 2)


my_coat = Coat(44)
print(f'Tissue consumption for my coat is {my_coat.get_consumption}')
my_suit = Suit(1.65)
print(f'Tissue consumption for my suit is {my_suit.get_consumption}')
print(f'Total tissue consumption is {my_suit.get_consumption + my_coat.get_consumption}')


class Cell:
    def __init__(self, num):
        try:
            if num <= 0:
                raise ValueError('num should be > 0')
            self.num = int(num)
        except TypeError:
            self.num = 1
            print('Check num value')
        except ValueError:
            print('Check num value')
            self.num = 1

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print('Subtraction is impossible')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.num // param) + '*' * (self.num % param)


cell_1 = Cell(12)
cell_2 = Cell(15)
print(cell_1.make_order(4))
print()
print(cell_2.make_order(5))

cell_3 = cell_2 - cell_1
print(cell_3)
print(cell_3.make_order(5))

print(Cell.__dict__)
