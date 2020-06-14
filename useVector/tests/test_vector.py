__author__ = "ハリネズミ"
import pytest
import math
from useVector.Vector import Vector


@pytest.fixture
def init_vector():
    """
    (5,2)のvectorオブジェクトを初期化
    :return:
    """
    vec = Vector([5, 2])
    return vec


@pytest.fixture
def init_vector2():
    """
    (3, 1)のvectorオブジェクトを初期化
    :return:
    """
    vec = Vector([3, 1])
    return vec


def test_vector_value(init_vector):
    """
    Vectorの初期化
    :return:
    """
    assert str(init_vector) == "(5, 2)"


def test_vector_len(init_vector):
    """
    Vectorの長さ
    :return:
    """
    assert 2 == len(init_vector)


def test_vector_first_value(init_vector):
    """
    Vectorの最初の要素を取得
    :param init_vector:
    :return:
    """
    assert 5 == init_vector[0]


def test_vector_addition(init_vector, init_vector2):
    """
    二つのVectorの足し算
    :param init_vector: (5,2)
    :param init_vector2: (3,1)
    :return:
    """
    assert str((8, 3)) == str(init_vector + init_vector2)


def test_vector_subtraction(init_vector, init_vector2) -> None:
    """
    二つのVectorの引き算
    :param init_vector: (5,2)
    :param init_vector2: (3,1)
    """
    assert str((2, 1)) == str(init_vector - init_vector2)


def test_vector_multiplication(init_vector) -> None:
    """
    Vectorの掛け算
    :param init_vector: (5,2)
    """
    assert str((10, 4)) == str(init_vector * 2)


def test_vector_r_multiplication(init_vector) -> None:
    """
    Vectorの掛け算
    :param init_vector: (5,2)
    """
    assert str((10, 4)) == str(2 * init_vector)


def test_vector_minus(init_vector):
    """
    Vectorのマイナス
    :param init_vector: (5,2)
    :return:
    """
    assert str((-5, -2)) == str(-init_vector)


def test_vector_zero():
    """
    全ての緯度の値が0のvectorを生成する
    :return:
    """
    zero2 = Vector.zero(2)
    assert str(zero2) == str((0, 0))


def test_vector_norm(init_vector):
    """
    vectorの長さ(ノルム)
    """
    vec = math.sqrt(sum(e**2 for e in Vector([5, 2])))
    assert vec == init_vector.norm()


def test_vector_unit_vector(init_vector):
    """
    単位Vector
    :param init_vector:
    :return:
    """
    assert init_vector.normalize().norm() == 1.0


def test_true():
    assert True


@pytest.mark.skip("Do not run this")
def test_false():
    """
    Skipサンプル
    :return:
    """
    assert False

