
import pytest
from unittest.mock import patch
from tornado.util import ArgReplacer


def test_valid_case_keyword():
    def func(a, b=10):
        return a + b
    
    replacer = ArgReplacer(func, 'b')
    old_value, args, kwargs = replacer.replace(new_value=20, args=(5,), kwargs={})
    assert len(args) == 1
    assert len(kwargs) == 1
    assert kwargs['b'] == 20
    result = func(*args, **kwargs)
    assert result == 25

def test_missing_argument():
    def func(a, b=10):
        return a + b
    
    replacer = ArgReplacer(func, 'b')
    old_value = replacer.get_old_value(args=(5,), kwargs={})
    assert old_value is None