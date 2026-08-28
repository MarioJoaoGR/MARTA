
import pytest
from ast import Constant
from apimd.parser import _e_type

def test_e_type_with_uniform_integers():
    """Test _e_type with a sequence of uniform integers."""
    result = _e_type([Constant(1), Constant(2)])
    assert result == '[int]'

def test_e_type_with_uniform_floats():
    """Test _e_type with a sequence of uniform floats."""
    result = _e_type([Constant(1.0), Constant(2.5)])
    assert result == '[float]'

def test_e_type_with_uniform_strings():
    """Test _e_type with a sequence of uniform strings."""
    result = _e_type([Constant('a'), Constant('b')])
    assert result == '[str]'

def test_e_type_with_uniform_booleans():
    """Test _e_type with a sequence of uniform booleans."""
    result = _e_type([Constant(True), Constant(False)])
    assert result == '[bool]'

def test_e_type_with_mixed_types_in_sequence():
    """Test _e_type with a sequence containing mixed types."""
    result = _e_type([Constant(1), Constant(2.0)])
    assert result == '[Any]'


def test_e_type_with_none_in_sequence():
    """Test _e_type with a sequence containing None."""
    result = _e_type([Constant(None)])
    assert result == '[NoneType]'

def test_e_type_with_multiple_sequences_of_uniform_types():
    """Test _e_type with multiple sequences of uniform types."""
    result = _e_type([Constant(1)], [Constant('a')], [Constant(3.0)])
    assert result == '[int, str, float]'

def test_e_type_with_no_arguments():
    """Test _e_type with no arguments."""
    result = _e_type()
    assert result == ''