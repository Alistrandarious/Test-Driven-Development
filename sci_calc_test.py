from sci_calc import *


def test_find_sqrt():
    assert find_sqrt(100) == 10.0
    assert find_sqrt(16) == 4.0
    assert find_sqrt(0) == 0
    assert find_sqrt(1) == 1


def test_find_ceil():
    assert find_ceil(12.7) == 13
    assert find_ceil(18.9) == 19
