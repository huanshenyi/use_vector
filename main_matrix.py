from useVector.Matrix import Matrix


if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)

    print(f"matrix.shape{matrix.shape()}") # matrix.shape(2, 2)
    print(matrix.size()) # 4
    print("len(matrix)={}".format(len(matrix))) # 2
    print("matrix[0][0]={}".format(matrix[0, 0])) # matrix[0][0]=1
    print("matrix")
