
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.parse import assert_cant_happen

def test_critical_missing_lines():
    with pytest.raises(ValueError) as exc_info:
        assert_cant_happen()
    assert str(exc_info.value) == 'Unexpected value'
