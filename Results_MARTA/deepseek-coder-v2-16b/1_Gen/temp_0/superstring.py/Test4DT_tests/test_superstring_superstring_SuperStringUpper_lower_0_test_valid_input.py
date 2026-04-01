
import pytest
from superstring.superstring import SuperStringUpper

def test_valid_input():
    str_upper = SuperStringUpper('Hello World')
    assert str_upper.lower() == 'hello world'
