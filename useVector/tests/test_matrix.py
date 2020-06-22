import pytest
from useVector.Matrix import Matrix


@pytest.fixture
def init_matrix():
    """
    マトリクスを初期化
    :return:
    """
    matrix = Matrix([[1, 2], [3, 4]])
    return matrix


def test_matrix_shape(init_matrix):
    """
    マトリクスのサイズ
    :return: 
    """
    assert (2, 2) == init_matrix.shape()


def test_matrix_get_item(init_matrix):
    """
    マトリクスの要素を取得
    :param init_matrix:
    :return:
    """
    assert init_matrix[0, 0] == 1
