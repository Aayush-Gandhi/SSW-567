from math import sqrt
from triangle import classify_triangle

def test_equilateral():
    assert classify_triangle(2, 2, 2) == "Equilateral"

def test_isosceles():
    assert classify_triangle(5, 5, 8) == "Isosceles"

def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_right_scalene_triplet_and_permutations():
    assert classify_triangle(3, 4, 5) == "Right"
    assert classify_triangle(4, 3, 5) == "Right"
    assert classify_triangle(5, 3, 4) == "Right"

def test_right_isosceles():
    s = sqrt(2)
    assert classify_triangle(1, 1, s) == "Right"

def test_not_a_triangle_degenerate_and_invalid():
    assert classify_triangle(1, 2, 3) == "Not a triangle"   # degenerate
    assert classify_triangle(0, 1, 1) == "Not a triangle"   # non-positive
