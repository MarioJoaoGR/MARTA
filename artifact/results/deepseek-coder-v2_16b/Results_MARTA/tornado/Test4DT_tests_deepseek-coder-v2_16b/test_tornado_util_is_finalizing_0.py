
import pytest
from tornado.util import is_finalizing


def test_empty_list():
    global L
    L = []
    assert not is_finalizing(), "Expected False when L is an empty list"