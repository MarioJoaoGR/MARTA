
import pytest
from unittest.mock import patch
from tornado.util import ArgReplacer


def test_invalid_input():
    def example_func(a, b):
        return a + b
    
    with pytest.raises(TypeError):
        replacer = ArgReplacer(example_func, 'b')
        replacer.replace(new_value=20, args=(5,))