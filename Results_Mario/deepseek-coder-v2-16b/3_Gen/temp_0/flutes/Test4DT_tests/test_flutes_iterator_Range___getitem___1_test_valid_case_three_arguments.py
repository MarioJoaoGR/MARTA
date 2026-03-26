
import pytest
from flutes.iterator import Range

def test_valid_case_three_arguments():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9
