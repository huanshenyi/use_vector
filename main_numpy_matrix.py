__author__ = "ハリネズミ"
import numpy as np

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    print(A)

    # マトリクスのshape
    print(A.shape) # (2, 2)
    # 転置行列
    print(A.T)
    """
    [[1 3]
     [2 4]]
    """
    # 要素取得
    print(A[1, 1]) # 4
    print(A[0]) # [1 2]
    print(A[:, 0]) # [1 3]
    print(A[1, :]) # [3 4]

    # マトリクスの基本計算
    B = np.array([[5, 6], [7, 8]])
    print(A + B)
    """
    [[ 6  8]
     [10 12]]
    """
    print(A - B)
    """
    [[-4 -4]
     [-4 -4]]
    """

    print(A * B) # でもこの計算は意味がない
    """
    [[ 5 12]
     [21 32]]
    """

    print(A.dot(B))
    """
    [[19 22]
     [43 50]]
    """

    p = np.array([10, 100])
    print(A + p) # 意味がない

    print(A.dot(p)) # [210 430]

    # 単位行列
    I = np.identity(2)
    print(I)
    """
    [[1. 0.]
     [0. 1.]]
    """
    print(A.dot(I))
    print(I.dot(A))

    # 正則行列
    invA = np.linalg.inv(A)
    print(invA)
    """
    [[-2.   1. ]
     [ 1.5 -0.5]]
     """
    print(invA.dot(A)) # 正則行列かける元の行列の結果は単位行列
    print(A.dot(invA))
