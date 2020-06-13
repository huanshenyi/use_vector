__author__ = "ハリネズミ"
import pytest


def test_true():
    assert True


@pytest.mark.skip("DO not run this")
def test_false():
    assert False


def test_key():
    a = ["a", "b"]
    b = ["b"]
    assert a == b
