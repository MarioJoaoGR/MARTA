# Module: youtube_dl.swfinterp
import pytest
from youtube_dl.swfinterp import _Multiname

# Test case to check initialization with 'variable' kind
def test_multiname_initialization_with_variable():
    mn_variable = _Multiname('variable')
    assert mn_variable.kind == 'variable', f"Expected 'variable' but got {mn_variable.kind}"

# Test case to check initialization with 'function' kind
def test_multiname_initialization_with_function():
    mn_function = _Multiname('function')
    assert mn_function.kind == 'function', f"Expected 'function' but got {mn_function.kind}"

# Test case to check initialization with 'class' kind
def test_multiname_initialization_with_class():
    mn_class = _Multiname('class')
    assert mn_class.kind == 'class', f"Expected 'class' but got {mn_class.kind}"
