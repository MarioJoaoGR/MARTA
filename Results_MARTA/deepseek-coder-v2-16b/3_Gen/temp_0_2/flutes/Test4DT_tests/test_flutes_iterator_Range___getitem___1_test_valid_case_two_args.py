
import pytest
from flutes.iterator import Range

def test_valid_case_two_args():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
