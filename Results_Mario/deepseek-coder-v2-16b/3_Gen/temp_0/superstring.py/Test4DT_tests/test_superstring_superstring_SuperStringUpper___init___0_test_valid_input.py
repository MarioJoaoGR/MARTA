
import pytest
from superstring.superstring import SuperStringUpper

def test_valid_input():
    instance = SuperStringUpper('base_string')
    assert hasattr(instance, '_base')
    assert getattr(instance, '_base') == 'base_string'
