import unittest

from ex_1_7 import Matrix


class TestCaseForEx17Matrix(unittest.TestCase):
    def test_create_matrix(self):
        mx = Matrix(5, 4).matrix
        result = [[0, 1, 2, 3, 4],
                  [0, 1, 2, 3, 4],
                  [0, 1, 2, 3, 4],
                  [0, 1, 2, 3, 4]]
        self.assertListEqual(mx, result)

    def test_turn_matrix_on_90(self):
        mx = Matrix(5, 4).move_matrix_on_90()
        result = [[0, 0, 0, 0],
                  [1, 1, 1, 1],
                  [2, 2, 2, 2],
                  [3, 3, 3, 3],
                  [4, 4, 4, 4]]
        self.assertListEqual(mx, result)


if __name__ == '__main__':
    unittest.main()
