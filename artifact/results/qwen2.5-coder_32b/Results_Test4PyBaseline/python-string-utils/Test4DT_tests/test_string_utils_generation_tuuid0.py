# Module: string_utils.generation
import pytest
from string_utils.generation import uuid
from uuid import UUID


def test_uuid_default_format():
    result = uuid()
    # Check that the result is a valid UUID in standard format with hyphens
    assert isinstance(result, str)
    assert len(result) == 36
    assert UUID(result).version == 4
    assert '-' in result

def test_uuid_hex_format():
    result = uuid(as_hex=True)
    # Check that the result is a valid UUID in hexadecimal format without hyphens
    assert isinstance(result, str)
    assert len(result) == 32
    assert UUID(hex=result).version == 4
    assert '-' not in result

def test_uuid_default_format_multiple_calls():
    results = [uuid() for _ in range(10)]
    # Check that multiple calls generate unique UUIDs
    assert len(results) == len(set(results))

def test_uuid_hex_format_multiple_calls():
    results = [uuid(as_hex=True) for _ in range(10)]
    # Check that multiple calls generate unique UUIDs in hexadecimal format
    assert len(results) == len(set(results))
