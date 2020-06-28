import numpy as np


if __name__ == "__main__":
   print(np.__version__)
   lst = [1, 2, 3]
   print(lst)
   vec = np.array([1, 2, 3])
   print(vec)

   # np.arrayを作る
   print(np.zeros(5)) # [0. 0. 0. 0. 0.]

   print(np.ones(5)) # [1. 1. 1. 1. 1.]

   print(np.full(5, 666)) # [666 666 666 666 666]

   #npの基本属性
   print(vec) # [1 2 3]

   print(f"size={vec.size}") # size = 3
   print(f"len={len(vec)}")  # len=3
   print(vec[0])          # 1
   print(vec[-1])         # 3
   print(vec[0:2])        # [1 2]
   print(type(vec[0:2]))  # <class 'numpy.ndarray'>

   # np.arrayの計算
   vec2 = np.array([4, 5, 6])
   print("{} + {} = {}".format(vec, vec2, vec+vec2))         # [1 2 3] + [4 5 6] = [5 7 9]
   print("{} - {} = {}".format(vec, vec2, vec-vec2))         # [1 2 3] - [4 5 6] = [-3 -3 -3]
   print("{} * {} = {}".format(2, vec, 2 * vec))             # 2 * [1 2 3] = [2 4 6]
   print("{} * {} = {}".format(vec, vec2, vec * vec2))       # [1 2 3] * [4 5 6] = [4 10 18]
   # ドット掛け算
   print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2))) # [1 2 3].dot([4 5 6]) = 32

   #ノルム求む
   print(np.linalg.norm(vec))     # 3.7416573867739413

   # 単位ベクトル
   print(vec / np.linalg.norm(vec))# [0.26726124 0.53452248 0.80178373]

   print(np.linalg.norm(vec / np.linalg.norm(vec))) # 単位ベクトルのノルムは 1.0
