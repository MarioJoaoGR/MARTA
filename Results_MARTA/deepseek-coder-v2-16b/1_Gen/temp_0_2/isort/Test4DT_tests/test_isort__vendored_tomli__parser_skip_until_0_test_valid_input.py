
import pytest
from isort._vendored.tomli._parser import skip_until

def test_valid_input():
    src = 'def myfunction(): pass'
    pos = 0
    expect = 'def'
    error_on = frozenset({' ', '\n'})
    error_on_eof = True
    
    result = skip_until(src, pos, expect, error_on=error_on, error_on_eof=error_on_eof)
    
    assert result == 0
