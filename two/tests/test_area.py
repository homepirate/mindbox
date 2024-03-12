import pytest
import math

from two.area import Circle, Triangle


def test_circle_area():
    circle = Circle(5)
    assert circle.area() == math.pi * 5**2


def test_circle_radius_type():
    with pytest.raises(TypeError):
        Circle("5")
    with pytest.raises(TypeError):
        Circle([5])


def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert triangle.area() == 6


def test_triangle_is_right_triangle():
    triangle1 = Triangle(3, 4, 5)
    assert triangle1.is_right_triangle() == True

    triangle2 = Triangle(6, 8, 10)
    assert triangle2.is_right_triangle() == True

    triangle3 = Triangle(3, 4, 6)
    assert triangle3.is_right_triangle() == False
