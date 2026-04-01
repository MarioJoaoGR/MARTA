
import pytest
from flutes.iterator import Range

def test_valid_case_one_arg():
    r = Range(10)
    assert len(r) == 10
