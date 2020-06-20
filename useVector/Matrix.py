from useVector.Vector import Vector


class Matrix:
    def __init__(self, list2d):
        self._value = [row[:] for row in list2d]

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
