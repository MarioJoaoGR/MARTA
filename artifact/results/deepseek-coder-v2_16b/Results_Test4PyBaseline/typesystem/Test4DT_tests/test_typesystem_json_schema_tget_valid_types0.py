
import pytest
import typing
from typesystem.json_schema import get_valid_types

def test_get_valid_types_single_type():
    result = get_valid_types({"type": "number"})
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], set)
    assert isinstance(result[1], bool)
    assert result[0] == {'number'}
    assert not result[1]

def test_get_valid_types_multiple_types():
    result = get_valid_types({"type": ["number", "string"]})
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], set)
    assert isinstance(result[1], bool)
    assert result[0] == {'number', 'string'}
    assert not result[1]

def test_get_valid_types_empty_type():
    result = get_valid_types({"type": []})
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], set)
    assert isinstance(result[1], bool)