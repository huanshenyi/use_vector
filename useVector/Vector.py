class Vector:
    def __init__(self, lst):
        # vectorの内容を保存する
        self._value = list(lst)

    def __getitem__(self, index):
        """Vectorの何個目の要素"""
        return self._value[index]

    def __len__(self):
        """Vectorの長さ(要素の個数)"""
        return len(self._value)

    def __repr__(self):
        # u > Vector([x, x])
        return f"Vector({self._value})"

    def __str__(self):
        # print(u) > (x, x)
        return f"({', '.join(str(e) for e in self._value)})"

    def __iter__(self):
        """
        vectorループ用
        :return:
        """
        return self._value.__iter__()

    def __add__(self, other):
        """
        Vectorの足し算
        other > 別のVector
        """
        # 現在のVectorとターゲットVectorの長さが一致することが前提とする
        assert len(self) == len(other), \
            "Error in adding . Length of vectors must be same"
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """
        Vectorの引き算
        :param other:
        :return:
        """
        # 現在のVectorとターゲットVectorの長さが一致することが前提とする
        assert len(self) == len(other), \
            "Error in adding . Length of vectors must be same"
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """
        掛け算 self * k
        :param k:
        :return:
        """
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """
        掛け算  k * self right
        :param k:
        :return:
        """
        return Vector([k * e for e in self])

    def __pos__(self):
        """
        Vectorのプラス値取得
        :return:
        """
        return 1 * self

    def __neg__(self):
        """
        Vectorのマイナス値を取得
        :return:
        """
        return -1 * self




