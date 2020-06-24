from useVector.Matrix import Matrix


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
