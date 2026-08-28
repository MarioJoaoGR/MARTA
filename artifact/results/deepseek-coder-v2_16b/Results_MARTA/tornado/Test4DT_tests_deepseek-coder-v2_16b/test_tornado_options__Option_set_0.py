
import pytest
from tornado.options import _Option, Error

# Test for invalid input type mismatch
def test_invalid_input_type_mismatch():
    opt = _Option(name='example_option', type=int, default=None, help='This is an example option')
    with pytest.raises(Error):
        opt.set('not_an_integer')
