
import pytest
from superstring.superstring import SuperStringUpper

def test_valid_input():
    instance = SuperStringUpper('example')
    assert hasattr(instance, '_base')
    assert instance._base == 'example'
