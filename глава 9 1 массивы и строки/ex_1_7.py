"""
Имеется изображение, представленное матрицей NxN; каждый пиксел
представлен 4 байтами. Напишите метод для поворота изображения на 90 градусов.
Удастся ли вам выполнить эту операцию «на месте»?
"""
from typing import List


MATRIX = List[List]


class Matrix:
    def __init__(self, n: int, m: int):
        self.matrix = self.create_matrix(n, m)

    def __str__(self):
        return f'matrix NxN {self.matrix}'

    def __repr__(self):
        return f'class: {Matrix.__name__}; type_matrix: {type(self.matrix)};' \
               f' size: {len(self.matrix)}; values: {type(self.matrix[0][0])}'

    def __eq__(self, other: list):
        return self.matrix == other

    @staticmethod
    def create_matrix(n: int, m: int) -> MATRIX:
        """
        Create matrix size MxN
        """
        if m == 0 or n == 0:
            raise TypeError('Matrix don`t zero size')
        return [[i for i in range(n)] for _ in range(m)]

    def move_matrix_on_90(self) -> MATRIX:
        """
        Turn matrix on 90 degrees
        """
        new_matrix = [[] for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                new_matrix[i].append(self.matrix[j][i])
        return new_matrix


if __name__ == '__main__':
    mx = Matrix(5, 4)
    print(mx)
    print(mx.move_matrix_on_90())
