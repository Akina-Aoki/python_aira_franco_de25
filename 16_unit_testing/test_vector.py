from pytest import raises, approx
from vector import Vector
import math


def test_valid_init():
    v = Vector(1, 2)
    assert v.numbers == (1, 2)


# TODO: you guys implement these until 11:30 and take some break also


# test negative values in init
def test_negative_valid_init():
    v = Vector(-1, -5, 3)
    assert v.numbers == (-1, -5, 3)


# test string in the init
def test_string_in_init_fails():
    with raises(TypeError):
        Vector("1")


# test len() function
def test_different_lengths():
    vectors = (Vector(1, 2), Vector(1), Vector(1, 2, 3), Vector(1, 2, 3, 4))
    expected_lengths = (2, 1, 3, 4)

    for vector, expected_length in zip(vectors, expected_lengths):
        assert len(vector) == expected_length


# test abs() function
def test_vector_norm_valid():
    v = Vector(1,4)
    expected_norm = math.sqrt(v[0]**2 + v[1]**2)

    assert abs(v) == approx(expected_norm)

def test_empty_vector_fail():
    with raises(ValueError):
        Vector()