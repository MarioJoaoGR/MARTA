
import pytest
from apimd.parser import parent

def test_parent_default_level():
    assert parent('a.b.c') == 'a.b'
    assert parent('x.y.z') == 'x.y'

def test_parent_custom_level():
    assert parent('a.b.c', level=2) == 'a'
    assert parent('x.y.z.w', level=3) == 'x'  # Corrected expected result

def test_parent_single_component():
    assert parent('single') == 'single'