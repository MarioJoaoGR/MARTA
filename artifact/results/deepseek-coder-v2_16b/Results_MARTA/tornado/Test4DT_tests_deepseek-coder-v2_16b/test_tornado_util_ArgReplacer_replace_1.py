
import pytest
from tornado.util import ArgReplacer



def test_invalid_input_types():
    def example_func(a, b=10):
        return a + b
    
    replacer = ArgReplacer(example_func, 'b')
    with pytest.raises(TypeError):
        replacer.replace(new_value='invalid', args=(5,))