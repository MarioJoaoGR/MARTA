
import pytest
from unittest.mock import patch

def assert_cant_happen():
    raise ValueError('Unexpected value')

@pytest.mark.parametrize("expected_exception, expected_message", [(ValueError, 'Unexpected value')])
def test_valid_input(expected_exception, expected_message):
    with pytest.raises(expected_exception) as exc_info:
        assert_cant_happen()
    assert str(exc_info.value) == expected_message
