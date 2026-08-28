
import pytest
from tornado.util import is_finalizing


def test_invalid_input():
    L = []
    assert is_finalizing() == False