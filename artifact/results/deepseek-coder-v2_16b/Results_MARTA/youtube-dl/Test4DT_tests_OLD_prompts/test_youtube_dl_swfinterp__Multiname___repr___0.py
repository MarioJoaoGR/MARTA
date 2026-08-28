
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.swfinterp import _Multiname

# Test 1: Initialize a multiname with 'simple' kind
def test_multiname_init_with_simple():
    mn = _Multiname(kind='simple')
    assert mn.kind == 'simple'

# Test 2: Initialize a multiname with 'qualified' kind
def test_multiname_init_with_qualified():
    mn = _Multiname(kind='qualified')
    assert mn.kind == 'qualified'

# Test 3: Initialize a multiname with an integer kind value
def test_multiname_init_with_integer_kind():
    mn = _Multiname(kind=0x1234)
    assert mn.kind == 0x1234

# Test 4: Check the repr of a multiname
def test_multiname_repr():
    mn = _Multiname(kind=0x1234)
    expected_repr = '[MULTINAME kind: 0x1234]'
    assert repr(mn) == expected_repr
