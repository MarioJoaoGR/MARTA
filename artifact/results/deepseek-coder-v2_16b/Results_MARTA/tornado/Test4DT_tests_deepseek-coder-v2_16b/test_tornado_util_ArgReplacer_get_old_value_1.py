
import pytest
from tornado.util import ArgReplacer



def test_missing_argument():
    def func(a, b=10):
        return a + b
    
    replacer = ArgReplacer(func, 'b')
    old_value = replacer.get_old_value(args=(5,), kwargs={})
    assert old_value is None