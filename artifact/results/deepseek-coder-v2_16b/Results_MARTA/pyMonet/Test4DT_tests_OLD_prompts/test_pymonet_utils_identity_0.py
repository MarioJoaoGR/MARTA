
import pytest
from pymonet.utils import identity

def test_identity_int():
    assert identity(5) == 5

def test_identity_str():
    assert identity("hello") == "hello"

def test_identity_list():
    assert identity([1, 2, 3]) == [1, 2, 3]
