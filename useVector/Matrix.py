from useVector.Vector import Vector


class Matrix:
    def __init__(self, list2d):
        self._value = [row[:] for row in list2d]

    @classmethod
    def zero(cls, r, c):
        """
        r行c列の0マトリクスを返す
        :param r:
        :param c:
        :return:
        """
        return cls([[0] * c for _ in range(r)])

    def T(self):
        """
        転置行列後のマトリクスを返す
        :return:
        """
        return Matrix([[e for e in self.col_vector(i)]
                       for i in range(self.col_num())])

    def __add__(self, another):
        """
        マトリクスの足し算
        :param another:もう一つマトリックス
        :return:
        """
        assert self.shape() == another.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Matrix([[a + b for a, b in zip(self.row_vector(i), another.row_vector(i))]] for i in range(len(self)))

    def __sub__(self, another):
        """
        マトリクスの引き算
        :param another: もう一つのマトリクス
        :return:
        """
        assert self.shape() == another.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Matrix([[a - b for a, b in zip(self.row_vector(i), another.row_vector(i))]] for i in range(len(self)))

    def dot(self, another):
        """
        マトリクスのドット掛け算
        :param another:
        :return: 掛け算の結果
        """
        if isinstance(another, Vector):
            # マトリクス掛けベクトル
            assert self.col_num() == len(another), \
                 "Error in Matrix-Vector Multiplication"
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])
        if isinstance(another, Matrix):
            # マトリクス掛けマトリクス
            assert self.col_num() == another.row_num(), \
                 "Error in Matrix-Matrix Multiplication"
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())]
                           for i in range(self.row_num())])

    def __mul__(self, k):
        """
        マトリクスの掛け算
        :param k:
        :return:
        """
        return Matrix([e * k for e in self.row_vector(i)] for i in range(len(self)))

    def __rmul__(self, k):
        """
        マトリクスの掛け算
        :param k:
        :return:
        """
        return self * k

    def __truediv__(self, k):
        """
        マトリクスの引き算
        :param k:
        :return:
        """
        return (1/k) * self

    def __pos__(self):
        """
        マトリクスのプラス値を返す
        :return:
        """
        return 1*self

    def __neg__(self):
        """
        マトリクスのマイナス値
        :return:
        """
        return -1 * self

    def row_vector(self, index):
        """
        第何行の内容
        :param index:
        :return:
        """
        return Vector(self._value[index])

    def col_vector(self, index):
        """
       　マトリクスのindex個の列vector
        :param index:
        :return:
        """
        return Vector([row[index] for row in self._value])

    def __getitem__(self, pos):
        """
        posはタブル、行列が入ってる
        マトリクスの特定の要素を返す
        :param pos:
        :return:
        """
        r, c = pos

        return self._value[r][c]

    def size(self):
        """
        マトリクスの要素数
        :return:
        """
        r, c = self.shape()
        return r * c

    def row_num(self):
        """
        マトリクスの行数
        :return:
        """
        return self.shape()[0]

    def col_num(self):
        """
        マトリクスの列数
        :return:
        """
        return self.shape()[1]

    def shape(self):
        """
        マトリクスの(行数、列数)
        :return:
        """
        return len(self._value), len(self._value[0])

    def __repr__(self):
        return "Matrix({})".format(self._value)

    __str__ = __repr__

    __len__ = row_num
