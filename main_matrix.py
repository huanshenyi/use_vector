from useVector.Matrix import Matrix
from useVector.Vector import Vector


if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)

    print(f"matrix.shape{matrix.shape()}") # matrix.shape(2, 2)
    print(matrix.size()) # 4
    print("len(matrix)={}".format(len(matrix))) # 2
    print("matrix[0][0]={}".format(matrix[0, 0])) # matrix[0][0]=1
    print("matrix")

    matrix2 = Matrix([[5, 6], [7, 8]])
    print("add:{}".format(matrix + matrix2)) # Matrix([[[6, 8]], [[10, 12]]])
    print("sub:{}".format(matrix - matrix2)) # Matrix([[[-4, -4]], [[-4, -4]]])
    print("scalar-mul:{}".format(matrix*2)) # scalar-mul:Matrix([[2, 4], [6, 8]])
    print("scalar-mul:{}".format(2 * matrix)) # scalar-mul:Matrix([[2, 4], [6, 8]])
    print(Matrix.zero(2, 3)) # Matrix([[0, 0, 0], [0, 0, 0]])

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print("T.dot(p) = {}".format(T.dot(p))) # T.dot(p) = (7.5, 6)

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print("T.dot(P) = {}".format(T.dot(P))) # T.dot(P) = Matrix([[0.0, 6.0, 7.5], [0, 0, 6]])

    print("A.dot(B) = {}".format(matrix.dot(matrix2))) # A.dot(B) = Matrix([[19, 22], [43, 50]])
    print("B.dot(A) = {}".format(matrix2.dot(matrix))) # B.dot(A) = Matrix([[23, 34], [31, 46]])

    print("P.T = {}".format(P.T())) # P.T = Matrix([[0, 0], [4, 0], [5, 3]])
    I = Matrix.identity(2)
    print('I=', I) # I= Matrix([[1, 0], [0, 1]])
    print("A.dot(I) = {}".format(matrix.dot(I)))
    print("I.dot(A) = {}".format(I.dot(Matrix)))

