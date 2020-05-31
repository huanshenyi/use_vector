class Vector:
    def __init__(self, list):
        # vectorの内容を保存する
        self._value = list

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
