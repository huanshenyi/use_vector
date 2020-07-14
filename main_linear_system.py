__author__ = "ハリネズミ"
from useVector.Matrix import Matrix
from useVector.Vector import Vector
from useVector.LinearSystem import LinearSystem
from useVector.LinearSystem import inv


if __name__ == "__main__":
    A = Matrix([[1, 2, 3], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()

    A7 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]])
    b7 = Vector([1, 5, 13, -1])
    ls7 = LinearSystem(A7, b7)
    ls7.gauss_jordan_elimination()
    ls7.fancy_print()

    A = Matrix([[1, 2], [3, 4]])
    invA = inv(A)
    print(invA)
    print(A.dot(invA))
    print(invA.dot(A))
