
import pytest
from unittest.mock import patch

def check_escaped_int(value: str) -> str:
    if not value.startswith('\\'):
        raise ValueError('Not an escaped int')
    try:
        int(value[1:])
    except ValueError as exc:
        raise ValueError('Not an escaped int') from exc
    else:
        return value[1:]

def test_invalid_input():
    with pytest.raises(ValueError) as e:
        check_escaped_int("abc")
    assert str(e.value) == 'Not an escaped int'
