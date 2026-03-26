
import pytest

from isort.output import _normalize_empty_lines

# Test cases for _normalize_empty_lines function

def test_normalize_two_empty_lines():
    result = _normalize_empty_lines(["", ""])
    assert result == ['']

def test_normalize_non_empty_and_one_empty_line():
    result = _normalize_empty_lines(["line1", "", "line2"])
    assert result == ['line1', '', 'line2', '']

def test_normalize_three_empty_lines():
    result = _normalize_empty_lines(["", "", ""])