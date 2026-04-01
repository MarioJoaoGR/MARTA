
import pytest

from isort.exceptions import AssignmentsFormatMismatch


def test_valid_input():
    code = 'x = 1\ny = 2'
    
    try:
        raise AssignmentsFormatMismatch(code)
    except AssignmentsFormatMismatch as e:
        assert e.code == code
