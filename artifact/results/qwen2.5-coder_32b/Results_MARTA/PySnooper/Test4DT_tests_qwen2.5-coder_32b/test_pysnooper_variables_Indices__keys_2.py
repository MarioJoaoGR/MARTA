
import pytest
from pysnooper.tracer import Tracer

class Indices:
    _slice = slice(None)

    def _keys(self, main_value):
        return range(len(main_value))[self._slice]

def test_keys_with_list():
    indices = Indices()
    main_list = [10, 20, 30]
    assert list(indices._keys(main_list)) == [0, 1, 2]

def test_keys_with_tuple():
    indices = Indices()
    main_tuple = (10, 20, 30)
    assert list(indices._keys(main_tuple)) == [0, 1, 2]

def test_keys_with_string():
    indices = Indices()
    main_string = "hello"
    assert list(indices._keys(main_string)) == [0, 1, 2, 3, 4]

def test_keys_with_custom_slice():
    indices = Indices()
    indices._slice = slice(1, 4)
    main_list = [10, 20, 30, 40, 50]
    assert list(indices._keys(main_list)) == [1, 2, 3]

def test_keys_with_custom_step():
    indices = Indices()
    indices._slice = slice(0, None, 2)
    main_list = [10, 20, 30, 40, 50]
    assert list(indices._keys(main_list)) == [0, 2, 4]
