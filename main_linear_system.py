__author__ = "ハリネズミ"
from useVector.Matrix import Matrix
from useVector.Vector import Vector
from useVector.LinearSystem import LinearSystem


if __name__ == "__main__":
    A = Matrix([[1, 2, 3], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()
