from find_root import *

def test_find_root_between_negative_and_positive_one():
    epsilon = 1e-6
    x = find_root(-1.0, 1.0, epsilon)
    assert abs(f(x)) < epsilon

