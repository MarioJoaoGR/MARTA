
import pytest
from tornado.util import ArgReplacer




def test_handle_argument_not_found():
    def example_func(a, b=10):
        return a + b
    
    replacer = ArgReplacer(example_func, 'c')
    old_value, args, kwargs = replacer.replace(new_value=20, args=(5,), kwargs={})
    assert old_value is None
    assert len(args) == 1 and args[0] == 5